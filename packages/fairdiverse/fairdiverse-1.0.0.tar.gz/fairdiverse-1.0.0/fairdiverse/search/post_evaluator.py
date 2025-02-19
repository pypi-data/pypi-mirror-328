import os
import re
import json
import numpy as np
import pandas as pd
import torch as th
import pickle
import torch
from .postprocessing_model.DESA import DESA
from .postprocessing_model.DALETOR import DALETOR
from .utils.utils import get_metrics_20

MAXDOC = 50
REL_LEN = 18


def evaluate_test_qids_DESA(model, test_tuple, div_q, mode='metric'):
    """
    Get the alpha-nDCG for the input query, the input document list are randomly shuffled.
    :param test_tuple: the features of the test query qid, test_turple = {}
    :param div_q: the div_query object of the test query qid
    :param qid: the id for the test query
    :return: the alpha-nDCG for the test query
    """

    metric = 0
    end = Max_doc_num = len(div_q.best_docs_rank)
    current_docs_rank = []
    if not test_tuple:
        return 0
    else:
        doc_mask = test_tuple['doc2vec_mask'].unsqueeze(0) # [1,50]
        sub_mask = test_tuple['sub2vec_mask'].unsqueeze(0) # [1,10]
        doc_emb = test_tuple['doc2vec'].unsqueeze(0).float() # [1, 50, 100]
        sub_emb = test_tuple['sub2vec'].unsqueeze(0).float() # [1,10,100]
        pos_qrel_feat = test_tuple['pos_qrel_feat'].unsqueeze(0).float() # [1,50,18]
        subrel_feat_mask = test_tuple['subrel_feat_mask'].unsqueeze(0)
        pos_subrel_feat = test_tuple['pos_subrel_feat'].unsqueeze(0).float() # [1,50,10,18]

        doc_mask.requires_grad = False
        sub_mask.requires_grad = False
        doc_emb.requires_grad = False
        sub_emb.requires_grad = False
        pos_qrel_feat.requires_grad = False
        subrel_feat_mask.requires_grad = False
        pos_subrel_feat.requires_grad = False

        if th.cuda.is_available():
            doc_mask, sub_mask, doc_emb, sub_emb, pos_qrel_feat, subrel_feat_mask, pos_subrel_feat =\
                doc_mask.cuda(), sub_mask.cuda(), doc_emb.cuda(), sub_emb.cuda(), pos_qrel_feat.cuda(), \
                subrel_feat_mask.cuda(), pos_subrel_feat.cuda()
        #print(doc_emb.shape, sub_emb.shape, doc_mask.shape, sub_mask.shape, pos_qrel_feat.shape, pos_subrel_feat.shape)
        score = model.fit(doc_emb, sub_emb, doc_mask, sub_mask, pos_qrel_feat, pos_subrel_feat, mode='Test')
        result = list(np.argsort(score[:len(test_tuple['doclist'])].cpu().detach().numpy()))
        if len(result) > 0:
            new_docs_rank = []
            for i in range(len(result)-1, -1, -1):
                new_docs_rank.append(test_tuple['doclist'][result[i]])
            #new_docs_rank = [test_tuple['doclist'][result[i]] for i in range(len(result)-1, len(result)-len(test_tuple['doclist'])-1, -1)]
            metric = div_q.get_test_alpha_nDCG(new_docs_rank)
    if mode == 'metric':
        return metric
    elif mode == 'both':
        return metric, new_docs_rank


def evaluate_test_qids_DALETOR(model, test_tuple, div_q, mode='metric'):
    """
    Evaluates the model on a set of test queries and returns the evaluation metric.
    
    :param model: The trained model to be evaluated.
    :param test_tuple: A tuple containing two elements - 
                       the first element is the input features (X),
                       and the second element is the relevance features (rel_feat).
    :param div_q: A `div_query` object that contains information about documents and subtopics.
    :param mode: The evaluation mode. It can be 'metric' (return only metric) or 'both' (return metric and ranked documents).
    :return: The evaluation metric (alpha-nDCG) or a tuple of the metric and the ranked documents, depending on the mode.
    """
    metric = 0
    end = Max_doc_num = len(div_q.best_docs_rank)
    current_docs_rank = []
    if test_tuple[0].shape[0] == 0:
        if mode == 'metric':
            return 0 
        else:
            return []
    else:
        X = test_tuple[0]
        rel_feat = test_tuple[1]
        X.requires_grad = False
        rel_feat.requires_grad = False
        X = X.reshape(1, X.shape[0], X.shape[1])
        rel_feat = rel_feat.reshape(1, rel_feat.shape[0], rel_feat.shape[1])
        
        if th.cuda.is_available():
            X = X.cuda()
            rel_feat = rel_feat.cuda()
        
        outputs = model.fit(X, rel_feat, False)
        out = outputs.cpu().detach().numpy().reshape(MAXDOC)
        # print('out.shape = ',out.shape)
        # print('out = ', out)
        result = np.argsort(-out[:end])
        # print('result =', result)

        for i in range(len(result)):
            if result[i] < Max_doc_num and result[i] not in current_docs_rank:
                current_docs_rank.append(result[i])

        if len(current_docs_rank)>0:
            new_docs_rank = [div_q.doc_list[i] for i in current_docs_rank]
            metric = div_q.get_test_alpha_nDCG(new_docs_rank)
            # print('qid = {}, metric = {}, mode = {}'.format(qid, metric, mode))
            if mode == 'metric':
                return metric
            elif mode == 'both':
                return metric, new_docs_rank


def get_global_fullset_metric(config):
    """
    Get the final metrics for the five fold best models.
    :param best_model_list: the best models for the five corresponding folds.
    :param test_qids_list: the corresponding test qids for five folds.
    """
    output_file = os.path.join(config['tmp_dir'], config['model'], 'run')
    if not os.path.exists(os.path.join(config['tmp_dir'], config['model'])):
        os.makedirs(os.path.join(config['tmp_dir'], config['model']))
    fout = open(output_file, 'w')
    all_models = config['best_model_list']
    qd = pickle.load(open(os.path.join(config['data_dir'], 'div_query.data'), 'rb'))
    with open(os.path.join(config['model_save_dir'], config['model'], 'fold_qid.json'), 'r') as f:
        test_qids_list = json.load(f)

    ''' get the metrics for five folds '''
    fold_time_pattern = re.compile(r'_FOLD_(\d+)_')
    for i in range(len(all_models)):
        model_file = all_models[i]
        fold_times = int(fold_time_pattern.search(all_models[i]).group(1))
        if config['model'].upper() == 'DESA':
            fold_p = os.path.join(config['data_dir'], config['model'], 'fold/')
            test_qids = test_dataset_dict = torch.load(os.path.join(fold_p, 'fold'+str(fold_times), 'test_data.pkl'))
            model = DESA(config['embedding_length'], 8, 2,config['embedding_length'], 8, 2, 8, config['dropout'])
            eval_func = evaluate_test_qids_DESA
        elif config['model'].upper() == 'DALETOR':
            from .datasets.DALETOR import get_test_dataset
            test_qids=test_qids_list[fold_times-1]
            test_dataset_dict = get_test_dataset(i+1, test_qids, config)
            model = DALETOR(0.0)
            eval_func = evaluate_test_qids_DALETOR
        
        model.load_state_dict(th.load(model_file))

        model.eval()
        if th.cuda.is_available():
            model = model.cuda()

        ''' ndeval test '''
        for qid in test_qids:
            metric, docs_rank = eval_func(model, test_dataset_dict[str(qid)], qd[str(qid)], 'both')
            if len(docs_rank)>0:
                for index in range(len(docs_rank)):
                    content = str(qid) + ' Q0 ' + str(docs_rank[index]) + ' ' + str(index+1) + ' -4.04239 indri\n'
                    fout.write(content)
    fout.close()
    csv_path = os.path.join(config['tmp_dir'], config['model'], 'result.csv')
    command = './search/eval/clueweb09/ndeval ./search/eval/clueweb09/2009-2012.diversity.ndeval.qrels ' + output_file + ' >' + str(csv_path)
    os.system(command)
    
    alpha_nDCG_20, NRBP_20, ERR_IA_20, S_rec_20 = get_metrics_20(csv_path)
    print('alpha_nDCG@20_std = {}, NRBP_20 = {}, ERR_IA_20 = {}, S_rec_20 = {}'.format(alpha_nDCG_20, NRBP_20, ERR_IA_20, S_rec_20))


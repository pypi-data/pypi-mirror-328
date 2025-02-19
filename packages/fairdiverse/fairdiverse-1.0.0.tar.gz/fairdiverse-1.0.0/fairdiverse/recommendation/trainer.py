import numpy as np
#from
import os

import pandas as pd
import yaml
import random

from .process_dataset import Process
from .base_model import MF, GRU4Rec, SASRec, BPR, BPR_Seq
from .rank_model import IPS, SDRO, Minmax_SGD, APR, FOCF, FairDual, Reg, FairNeg, DPR

import time
import torch.optim as optim

from .sampler import PointWiseDataset, PairWiseDataset, RankingTestDataset, SequentialDataset
from .evaluator import CTR_Evaluator, Ranking_Evaluator

from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm,trange
from datetime import datetime
import torch
import json
from scipy.sparse import save_npz, load_npz
import torch.nn as nn
import ast



class RecTrainer(object):
    def __init__(self, train_config):
        """Initialize In-processing and base models.

        :param train_config: Your custom config files.
        """

        self.dataset = train_config['dataset']
        #self.stage = stage
        self.train_config = train_config


    def load_configs(self, dir):
        """
            Loads and merges configuration files for the model, dataset, and evaluation.

            This function loads multiple YAML configuration files, including the process configuration,
            dataset-specific settings, model configurations, and evaluation parameters. All configurations
            are merged, with the highest priority given to the class's own `config` attribute.

            :param dir: The directory where the main process configuration file is located.
            :return: A dictionary containing the merged configuration from all files.
        """


        print("start to load config...")
        with open(os.path.join(dir, "process_config.yaml"), 'r') as f:
            config = yaml.safe_load(f)


        # print(train_data_df.head())

        print("start to load model...")
        with open(os.path.join("recommendation", "properties", "models.yaml"), 'r') as f:
            model_config = yaml.safe_load(f)

        with open(os.path.join("recommendation", "properties", "models", self.train_config['model'] + ".yaml"),
                  'r') as f:
            model_config.update(yaml.safe_load(f))

        if self.train_config['fair-rank'] == True:
            with open(os.path.join("recommendation", "properties", "models", self.train_config['rank_model'] + ".yaml"),
                      'r') as f:
                model_config.update(yaml.safe_load(f))

        config.update(model_config)

        with open(os.path.join("recommendation", "properties", "evaluation.yaml"), 'r') as f:
            config.update(yaml.safe_load(f))

        config.update(self.train_config)  ###train_config has highest rights
        print("your loading config is:")
        print(config)

        return config

    def Set_Dataset(self, data_type, config, train_data_df, val_data_df, test_data_df):
        """
            Initializes and returns the training, validation, and test datasets based on the specified data type and evaluation type.

            This function creates appropriate dataset objects for training, validation, and testing based on the provided data type
            (point, pair, or sequential) and the evaluation type (CTR or ranking). It supports different dataset types for training
            and evaluation, and raises an error if an unsupported type is provided.

            :param data_type: The type of dataset to be used for training. Must be one of ['point', 'pair', 'sequential'].
            :param config: A configuration dictionary that contains parameters for dataset creation and evaluation type.
            :param train_data_df: The DataFrame containing the training data.
            :param val_data_df: The DataFrame containing the validation data.
            :param test_data_df: The DataFrame containing the test data.
            :return: A tuple containing the training, validation, and test datasets.
        """
        if data_type == 'point':
            train = PointWiseDataset(train_data_df, config)
        elif data_type == 'pair':
            train = PairWiseDataset(train_data_df, config)
        elif data_type == 'sequential':
            train = SequentialDataset(train_data_df, config)
        else:
            raise NotImplementedError("train_type only supports in [point, pair, sequential]")

        if config['eval_type'] == 'CTR':
            valid = PointWiseDataset(val_data_df, config)
            test = PointWiseDataset(test_data_df, config)
        elif config['eval_type'] == 'ranking':
            valid = RankingTestDataset(val_data_df, config)
            test = RankingTestDataset(test_data_df, config)
        else:
            raise NotImplementedError("We only support the eval type as [CTR, ranking]")

        return train, valid, test

    def check_model_stage(self,config, Model):
        """
            Checks if the provided data type in the configuration aligns with the supported model type.

            This function verifies that the data type specified in the `config` dictionary is compatible with the model's
            supported types. If the data type is not supported by the model, a `ValueError` is raised with an informative message.

            :param config: A configuration dictionary that includes the data type used for testing.
            :param Model: The model class or object which has a `type` attribute specifying the supported data types.
        """
        if config['data_type'] not in Model.type:
            raise ValueError(f"The tested data type does not align with the model type: input is {config['data_type']}, "
                             f"the model only support: {Model.type}")

    def train(self):
        """
            Training in-processing and base model main workflow.
        """

        dir = os.path.join("recommendation", "processed_dataset", self.dataset)

        state = Process(self.dataset, self.train_config)
        config = self.load_configs(dir)
        print(state)
        #exit(0)

        print("start to load dataset......")

        self.device = config['device']

        if config['model'] == 'mf':
            self.Model = MF(config).to(self.device)
        elif config['model'] == 'BPR':
            self.Model = BPR(config).to(self.device)
        elif config['model'] == 'BPR_Seq':
            self.Model = BPR_Seq(config).to(self.device)
        elif config['model'] == 'gru4rec':
            self.Model = GRU4Rec(config).to(self.device)
        elif config['model'] == 'SASRec':
            self.Model = SASRec(config).to(self.device)

        else:
            raise NotImplementedError(f"Not supported model type: {config['model']}")

        self.check_model_stage(config, self.Model)

        self.group_weight = np.ones(config['group_num'])





        train_data_df = pd.read_csv(os.path.join(dir, self.dataset + ".train"), sep='\t')
        val_data_df = pd.read_csv(os.path.join(dir, self.dataset + ".valid." + config['eval_type']), sep='\t')
        test_data_df = pd.read_csv(os.path.join(dir, self.dataset + ".test." + config['eval_type']), sep='\t')

        print(test_data_df.head())
        train_data_df["history_behaviors"] = train_data_df["history_behaviors"].apply(lambda x: np.array(ast.literal_eval(x)))
        val_data_df["history_behaviors"] = val_data_df["history_behaviors"].apply(lambda x: np.array(ast.literal_eval(x)))
        test_data_df["history_behaviors"] = test_data_df["history_behaviors"].apply(lambda x: np.array(ast.literal_eval(x)))

        optimizer = optim.Adam(self.Model.parameters(), lr= config['learning_rate'])
        data_type = config['data_type']



        train, valid, test = self.Set_Dataset(data_type, config, train_data_df, val_data_df, test_data_df)

        if config['fair-rank'] == True:
            if config['data_type'] == 'point':
                raise ValueError(
                    "fair ranking model only supports the pair and sequential data_type, not the point type")

            if config['rank_model'] == "IPS":
                self.Fair_Ranker = IPS(config, self.group_weight)

            elif config['rank_model'] == 'SDRO':
                self.Fair_Ranker = SDRO(config, self.group_weight)

            elif config['rank_model'] == 'Minmax_SGD':
                self.Fair_Ranker = Minmax_SGD(config, self.group_weight)

            elif config['rank_model'] == 'APR':
                self.Fair_Ranker = APR(config, self.group_weight)

            elif config['rank_model'] == 'FOCF':
                self.Fair_Ranker = FOCF(config, self.group_weight)

            elif config['rank_model'] == 'FairDual':
                self.Fair_Ranker = FairDual(config, self.group_weight)

            elif config['rank_model'] == 'Reg':
                self.Fair_Ranker = Reg(config, self.group_weight)

            elif config['rank_model'] == 'FairNeg':
                self.Fair_Ranker = FairNeg(config, train.user2pos)

            elif config['rank_model'] == 'DPR':
                self.Fair_Ranker = DPR(config, self.group_weight)

            else:
                NotImplementedError(f"Not supported fair rank model type:{config['rank_model']}")

            self.check_model_stage(config, self.Fair_Ranker)
            if self.Fair_Ranker.fair_type == "sample" and config['data_type'] != "pair":
                raise ValueError(
                    f"The choosed fair ranker [{config['rank_model']}] only support the base model type as pair")


        train_loader = DataLoader(train, batch_size=config['batch_size'], shuffle=True)
        valid_loader = DataLoader(valid, batch_size=config['eval_batch_size'], shuffle=False)
        test_loader = DataLoader(test, batch_size=config['eval_batch_size'], shuffle=False)

        if config['eval_type'] == 'CTR':
            evaluator = CTR_Evaluator(config)
        elif config['eval_type'] == 'ranking':
            evaluator = Ranking_Evaluator(config)
        else:
            raise NotImplementedError("we only support eval type in [CTR, ranking] !")

        today = datetime.today()
        today_str = f"{today.year}-{today.month}-{today.day}"
        log_dir = os.path.join("recommendation", "log", f"{today_str}_{config['log_name']}")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        print("start to train...")

        for epoch in trange(config['epoch']):


            total_loss = 0
            self.Model.train()
            best_result = -1

            if config['fair-rank'] == True:
                if 'update_epoch' in config and epoch % config['update_epoch'] == 0:
                    if config['rank_model'] == 'FairDual':
                        self.Fair_Ranker.reset_parameters(len(train_data_df))
                    else:
                        self.Fair_Ranker.reset_parameters()

            #for user_ids, item_ids, group_ids, label in train_loader:
            for train_datas in train_loader:

                if data_type == "point":
                    interaction = {"user_ids": train_datas[0].to(self.device), "history_ids": train_datas[1].to(self.device),
                                   "item_ids": train_datas[2].to(self.device),
                                   "group_ids": train_datas[3].to(self.device), "label": train_datas[4].to(self.device)}
                    #ids = {"user_ids": train_datas[0].to(self.device), "item_ids": train_datas[1].to(self.device)}
                elif data_type == "pair":
                    interaction = {"user_ids": train_datas[0].to(self.device), "history_ids": train_datas[1].to(self.device),
                                   "item_ids": train_datas[2].to(self.device), "neg_item_ids": train_datas[3].to(self.device),
                                   "group_ids": train_datas[4].to(self.device), "neg_group_ids": train_datas[5].to(self.device)
                                   }
                    #ids = {"user_ids": train_datas[0].to(self.device), "item_ids": train_datas[1].to(self.device)}
                else: ###squential format
                    interaction = {"user_ids": train_datas[0].to(self.device), "history_ids": train_datas[1].to(self.device),
                                   "item_ids": train_datas[2].to(self.device), "group_ids": train_datas[3].to(self.device), }

                feed_user_dict = {"user_ids": train_datas[0].to(self.device), "history_ids": train_datas[1].to(self.device)}
                feed_item_ids = train_datas[2].to(self.device)

                optimizer.zero_grad()
                #loss = self.Model.compute_loss(interaction)

                if config['fair-rank'] == True:

                    if self.Fair_Ranker.fair_type == 're-weight':
                        loss = self.Model.compute_loss(interaction)
                        scores = self.Model(feed_user_dict, feed_item_ids)


                        input_dict = {'items': train_datas[2].detach().numpy(), 'loss': loss.detach().cpu().numpy(),
                                      'scores': scores.detach().cpu().numpy()}

                        if config['rank_model'] == 'FairDual':
                            ## FairDual needs sample some items
                            exposure_sample_num = config['exposure_sample_num']
                            item_sample_ids = random.sample(range(config['item_num']), exposure_sample_num)
                            item_sample_ids = torch.tensor(item_sample_ids, dtype=torch.long).to(self.device)

                            scores, indices = self.Model.full_ranking(feed_user_dict, item_sample_ids, k=config['s_k'])

                            items = item_sample_ids[indices.detach().cpu().numpy()]
                            input_dict['sample_items'] = items

                        weight = self.Fair_Ranker.reweight(input_dict=input_dict)
                        #print(weight)
                        loss = torch.mean(torch.tensor(weight).to(self.device)*loss)

                    elif self.Fair_Ranker.fair_type == "sample":
                        neg_item_ids, adj = self.Fair_Ranker.sample(interaction, self.Model)
                        interaction['neg_item_ids'] = neg_item_ids
                        loss = self.Model.compute_loss(interaction)
                        if config['rank_model'] == "FairNeg":
                            group_loss = loss.detach().cpu().numpy()
                            group_loss = np.matmul(group_loss, adj)/(np.sum(adj, axis=0, keepdims=False)+1)
                            self.Fair_Ranker.accumulate_epoch_loss(group_loss)


                        loss = torch.mean(loss)

                    elif self.Fair_Ranker.fair_type == "regularizer":
                        loss = self.Model.compute_loss(interaction)
                        scores = self.Model(feed_user_dict, feed_item_ids)
                        input_dict = {'items': train_datas[2], 'loss': loss, 'scores':scores}

                        if config['rank_model'] == 'DPR':
                            input_dict = {'item_ids': train_datas[2].to(self.device), 'scores': scores,
                                          "neg_item_ids": train_datas[3].to(self.device),
                                          "group_ids": train_datas[4].to(self.device),
                                          "neg_group_ids": train_datas[5].to(self.device)
                                          }
                            fair_loss = self.Fair_Ranker.fairness_loss(input_dict, self.Model)
                            loss = torch.mean(loss) + fair_loss

                        else:
                            fair_loss = self.Fair_Ranker.fairness_loss(input_dict)
                            loss = torch.mean(loss) + config['fair_lambda'] * fair_loss

                    else: ##other type of fairness method, which modifies embeddings during the evaluation process
                        loss = self.Model.compute_loss(interaction)
                        loss = torch.mean(loss)

                else:
                    loss = self.Model.compute_loss(interaction)
                    loss = torch.mean(loss)

                loss.backward()
                optimizer.step()
                total_loss += loss.item()



            if epoch % config['eval_step'] == 0:
                eval_result = evaluator.eval(valid_loader, self.Model)
                watch_eval_value = eval_result[config['watch_metric']]
                if watch_eval_value >= best_result:
                    best_result = watch_eval_value
                    torch.save(self.Model.state_dict(), os.path.join(log_dir, "best_model.pth"))
                print(f"eval result: {eval_result}, best result: {best_result}")
                print()


            print("epoch: %d loss: %.3f" %(epoch, total_loss/ len(train_loader)))



        print(f"training complete! start to save the config and model...")
        print(f" config files are dump in {log_dir}")
        with open(os.path.join(log_dir, "config.yaml"), 'w') as f:
            yaml.dump(config, f)

        print("start to testing...")
        self.Model.load_state_dict(torch.load(os.path.join(log_dir, "best_model.pth")))  # load state_dict
        self.Model.eval()  # change to eval model
        if config['store_scores'] == False:
            test_result = evaluator.eval(test_loader, self.Model)
        else:
            test_result, coo_matrix = evaluator.eval(test_loader, self.Model, store_scores=True)
            save_npz(os.path.join(log_dir, 'ranking_scores.npz'), coo_matrix) ##prepared for re-ranking stage


        with open(os.path.join(log_dir, 'test_result.json'), 'w') as file:
            json.dump(test_result, file)
        print(test_result)
        print(f"dump in {log_dir}")



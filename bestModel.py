from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

class BestTuner:

    def __init__(self):
        self.clf = RandomForestClassifier()
        self.xgb = XGBClassifier(objective='binary:logistic')


    def get_best_randomForest_params(self,x_train,y_train):
        self.param_grid = {"n_estimators": [10, 50, 100, 130], "criterion": ['gini', 'entropy'],
                        "max_depth": range(2, 4, 1), "max_features": ['auto', 'log2']}

        self.grid = GridSearchCV(estimator=self.clf, param_grid=self.param_grid, cv=5, verbose=3)
        self.grid.fit(x_train, y_train)
        estimator = self.grid.best_params_['n_estimators']
        criterion = self.grid.best_params_['criterion']
        max_depth = self.grid.best_params_['max_depth']
        max_features = self.grid.best_params_['max_features']
        model=RandomForestClassifier(n_estimators = estimator,
                                     criterion = criterion,
                                     max_depth =max_depth,
                                     max_features = max_features)
        model.fit(x_train, y_train)
        return model


    def get_best_xgboost_params(self,x_train,y_train):
        self.param_grid = {'learning_rate': [0.5, 0.1, 0.01, 0.001],
                                    'max_depth': [3, 5, 10, 20],
                                    'n_estimators': [10, 50, 100, 200]
        }

        self.grid = GridSearchCV(estimator=self.xgb, param_grid=self.param_grid, cv=5, verbose=3)
        self.grid.fit(x_train, y_train)
        learning_rate = self.grid.best_params_['learning_rate']
        max_depth = self.grid.best_params_['max_depth']
        n_estimators = self.grid.best_params_['n_estimators']

        model=XGBClassifier(n_estimators = n_estimators,
                            max_depth =max_depth,
                            learning_rate = learning_rate)
        model.fit(x_train, y_train)
        return model


    def getBestModel(self,x_train, x_test, y_train, y_test):
        self.randomForestModel = self.get_best_randomForest_params(x_train, y_train)
        self.randForest_predict = self.randomForestModel.predict(x_test)

        if (len(y_test.unique() == 1)):
            self.randForest_score = accuracy_score(self.randForest_predict, y_test)
        else:
            self.randForest_score = roc_auc_score(self.randForest_predict, y_test)

        self.xgboostModel = self.get_best_xgboost_params(x_train,y_train)
        self.xgboost_predict = self.xgboostModel.predict(x_test)
        if (len(y_test.unique() ==1)):
            self.xgboost_score = accuracy_score(self.xgboost_predict,y_test)
        else:
            self.xgboost_score = roc_auc_score(self.xgboost_predict,y_test)

        if (self.randForest_score > self.xgboost_score):
            return self.randomForestModel,"randomForest"
        else:
            return self.xgboostModel,"xgboost"
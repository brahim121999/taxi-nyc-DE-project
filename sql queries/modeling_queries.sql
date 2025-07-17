-- Training with BOOSTED TREE REGRESSOR
CREATE OR REPLACE MODEL `taxi-project-461423.ml_dataset.boosted_tree_model`
  OPTIONS (model_type="BOOSTED_TREE_REGRESSOR", enable_global_explain=TRUE, input_label_cols=["total_amount"])
AS
SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_train_data`;


SELECT COUNT(*) FROM `taxi-project-461423.ml_dataset.preprocessed_test_data`;


-- Evaluate the trained model with the test data
SELECT * FROM
ML.EVALUATE(MODEL `taxi-project-461423.ml_dataset.boosted_tree_model`,
(SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_test_data`));


-- Example for making predictions from the model
SELECT * FROM
ML.PREDICT (MODEL `taxi-project-461423.ml_dataset.boosted_tree_model`,
(SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_test_data` LIMIT 10));


-- Query the model's global explanations
SELECT * FROM ML.GLOBAL_EXPLAIN(MODEL `taxi-project-461423.ml_dataset.boosted_tree_model`);









-- Training with RANDOM FOREST REGRESSOR
CREATE OR REPLACE MODEL `taxi-project-461423.ml_dataset.random_forest_model`
  OPTIONS (model_type="RANDOM_FOREST_REGRESSOR", enable_global_explain=TRUE, input_label_cols=["total_amount"])
AS
SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_train_data`;

-- Evaluate the trained model with the test data
SELECT * FROM
ML.EVALUATE(MODEL `taxi-project-461423.ml_dataset.random_forest_model`,
(SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_test_data`));










-- Training with DNN REGRESSOR
CREATE OR REPLACE MODEL `taxi-project-461423.ml_dataset.dnn_regressor`
  OPTIONS (model_type="DNN_REGRESSOR", enable_global_explain=TRUE, input_label_cols=["total_amount"])
AS
SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_train_data`;

-- Evaluate the trained model with the test data
SELECT * FROM
ML.EVALUATE(MODEL `taxi-project-461423.ml_dataset.dnn_regressor`,
(SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_test_data`));









-- Training with AUTOML REGRESSOR
CREATE OR REPLACE MODEL `taxi-project-461423.ml_dataset.automl_regressor`
  OPTIONS (model_type="AUTOML_REGRESSOR", enable_global_explain=TRUE, input_label_cols=["total_amount"])
AS
SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_train_data`;

-- Evaluate the trained model with the test data
SELECT * FROM
ML.EVALUATE(MODEL `taxi-project-461423.ml_dataset.automl_regressor`,
(SELECT * FROM `taxi-project-461423.ml_dataset.preprocessed_test_data`));



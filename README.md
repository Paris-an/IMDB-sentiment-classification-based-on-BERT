# IMDB-sentiment-classification-based-on-BERT
IMDB film review sentiment classification based on BERT's supervised learning model. On the other hand, the model can be extended to other natural language multi-classification tasks.

---------------------------------------
ALL_OUTPUT:4组实验运行结果。

BERT_BASE_DIR:谷歌预训练BERT模型文件。

DATA_DIR:训练集、验证集、测试集文件。

output_models:运行程序时存储输出文件。

Raw_Data:原始数据集以及数据预处理过程涉及到的一些数据文件。

IMDB Parameters:运行‘run.py’文件时需将该文件中的参数传入程序。

run.py:训练、验证、测试模型时运行的文件。

-------------------------------------------
  --task_name=mrpc \
  --do_train=true \
  --do_eval=true \
  --do_predict=true \
  --data_dir=D:\XXXXXXX\IMDB\DATA_DIR
  --vocab_file=BERT_BASE_DIR/vocab.txt \
  --bert_config_file=BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=30 \
  --train_batch_size=1 \
  --learning_rate=2e-6 \
  --num_train_epochs=5 \
  --output_dir=output_models/

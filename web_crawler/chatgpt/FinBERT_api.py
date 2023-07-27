from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import os


def FinBERT_ESG(text: str):
    if not os.path.exists(r'./FinBERT_Tone'):
        print('FinBERT_Tone模型不存在，请先下载！')
        quit()

    # 导入FinBERT_ESG模型
    finbert_esg = BertForSequenceClassification.from_pretrained(r'./FinBERT_ESG',num_labels=4)
    tokenizer_esg = BertTokenizer.from_pretrained(r'./FinBERT_ESG')

    nlp_esg = pipeline("text-classification", model=finbert_esg, tokenizer=tokenizer_esg)
    results = nlp_esg(text)
    return results


def FinBERT_sentiment(text: str):
    if not os.path.exists(r'./FinBERT_Tone'):
        print('FinBERT_Tone模型不存在，请先下载！')
        quit()

    # 导入FinBERT_sentiment模型
    finbert_sentiment = BertForSequenceClassification.from_pretrained(r'./FinBERT_Tone',num_labels=3)
    tokenizer_sentiment = BertTokenizer.from_pretrained(r'./FinBERT_Tone')

    nlp_sentiment = pipeline("sentiment-analysis", model=finbert_sentiment, tokenizer=tokenizer_sentiment)
    results_sentiment = nlp_sentiment(text)
    return results_sentiment


if __name__ == '__main__':


    # 测试是否成功导入
    results = FinBERT_ESG('Rhonda has been volunteering for several years for a variety of charitable community programs.')
    if(results[0]['label']=='Social'):
        print("--------------FinBERT_ESG模型导入成功！--------------")

    test_sentences = ["there is a shortage of capital, and we need extra financing",  
                "growth is strong and we have plenty of liquidity", 
                "there are doubts about our finances", 
                "profits are flat"]
    results_sentiment = FinBERT_sentiment(test_sentences)
    if(results_sentiment[0]['label']=='Negative'):
        print("--------------FinBERT_sentiment模型导入成功！--------------")
import re
import string


# string 문자열 필터링
def text_string(texts:str) -> str:
    f"""texts 문자열 필터링
    (내용) : 이모티콘, 특수기호 필터링 -> .map() 활용용 함수
    (tokenizer) : [ 0-9A-zㄱ-힣{re.escape(string.punctuation)}]
    """
    pattern = f"[ 0-9A-zㄱ-힣{re.escape(string.punctuation)}]"
    tokenizer = re.findall(pattern, texts)
    return "".join(tokenizer)

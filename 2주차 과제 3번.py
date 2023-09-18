import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    emails = re.findall(pattern, text)
    
    return emails

if __name__ == '__main__':
    text = input("텍스트를 입력하세요: ")
    
    found_emails = extract_emails(text)
    
    if found_emails:
        print("추출된 이메일 주소:")
        for email in found_emails:
            print(email)
    else:
        print("이메일 주소가 발견되지 않았습니다.")
    
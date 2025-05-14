from crawling.scrap import get_current_price

# 종목 코드와 이름 매핑한 딕셔너리
stock_name_dict = {
'005930': '삼성전자',
'000660': 'SK하이닉스',
'035420': 'NAVER',
'005380': '현대차',
'207940': '삼성바이오로직스',
'051910': 'LG화학',
'035720': '카카오'
# 필요 시 여기에 더 추가
}

if __name__ == "__main__":
    user_code = input("종목 코드를 입력하세요 (예: 005930):").strip()
    stock_name = stock_name_dict.get(user_code, "알 수 없는 종목")
    current_price = get_current_price(user_code)
    print(f"[{stock_name} ({user_code})] 현재가: {current_price}원")
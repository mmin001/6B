import requests
from bs4 import BeautifulSoup
import time

def scrape_menus():
    stores=[
        {'name': "공식당", 'url': "https://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno=86&selDate=2025-12-15"},
    ]
    headers= {'User-Agent': 'Mozilla/5.0'}
    all_data = []
    for store in stores:
        try:
            response = requests.get(store['url'], headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            tables = soup.find_all('table', class_='tstyle_me')
            if not tables:
                print(f"[{store['name']}]테이블이 존재하지 않습니다.")
                continue
            date_th = tables[0].find('thead').find_all('th')
            dates = [th.get_text(" ", strip=True) for th in date_th[1:]]
            meal_type = [('중식', tables[1]), ('석식', tables[2])]
            for meal_name, table in meal_type:
                tds = table.find('tbody').find_all('td')
                for i, td in enumerate(tds):
                    if i>=len(dates): break
                    current_date_info = dates[i]
                    items = td.find_all('li')
                    for item in items:
                        raw_text = item.get_text(" ", strip=True)
                        
                        if '￦' in raw_text:
                            parts = raw_text.split('￦')
                            name_part = parts[0].strip()
                            price_part = parts[1].strip()
                            
                            has_pork = '★' in name_part
                            clean_name = name_part.replace('★', '').strip()
                            
                            if "운영시간" in clean_name:
                                clean_name = clean_name.split('운영시간')[0].strip()
                            price_str = price_part.split()[0].replace(',', '')
                            menu_item = {
                                '식당명' : store['name'],
                                '날짜' : current_date_info,
                                '구분' : meal_name,
                                '메뉴명' : clean_name,
                                '가격' : int(price_str),
                                '돼지고기포함' : has_pork,
                                
                            }
                            all_data.append(menu_item)

        except Exception as e:
            print(f"에러 발생: {e}")
    return all_data        

            
       
if __name__ =="__main__":
    results = scrape_menus()
    for r in results:
        print(r)
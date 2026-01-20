import scraper
import databasemanager
def main():
    print("--테스트 시작--")
    try:
        databasemanager.init_db()
        
        print("데이터 가져오는 중")
        scraped_data = scraper.scrape_menus()
        
        if scraped_data:
            databasemanager.save_to_db(scraped_data)
            print(f"총 {len(scraped_data)}개의 메뉴를 성공적으로 저장했습니다")
        else:
            print("저장할 데이터가 없습니다")
            return
        print("---저장된 데이터 확인---")
        get_data = databasemanager.get_all_menus()
        for d in get_data:
            print(d)
    
    except Exception as e:
        print(f"에러발생 : {e}")
        import traceback
        traceback.print_exc()
        
        
if __name__=="__main__":
    main()
    
    
    
    
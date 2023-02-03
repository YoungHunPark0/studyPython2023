import code28_module_name #code28 의 내용을 불러와야 

print(f'code29_module_main : {__name__}') # 이것만실행하면 code28과 같은 __main__뜸
            #__main__ 나의 이름을 알리는 특수 
# C언어에서 int main(void) 동일 같음
if __name__ == '__main__':  # 자주사용
    print('main을 실행합니다')
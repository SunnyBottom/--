def test_function():        # 1
    def inner_function():   # 2
        print("Я в области видимости функции test_function")

    inner_function()        # 3 - Не возвращает
inner_function()  #Не работает и выдает ошибку
#Мы не можем доставать значения внутри функции
test_function()     #Работает
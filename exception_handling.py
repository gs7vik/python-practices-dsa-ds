import logging
values=[0,1,2,3,'a']
for value in values:
    try:
        print(10/value)
        raise AttributeError #used to manually trigger an exception
    except (ValueError, ZeroDivisionError) as e: #when you want to give the same message for 2 exceptions you can combine them
        print(str(e))
    except Exception as e: #covering broad exceptions here 
        logging.exception(e)
        
print("hello")
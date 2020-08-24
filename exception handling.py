while(1):

    try:
        x=int(input('enter first numbber'))
        y=int(input('enter second number'))
        z=x/y
        print(z)

    except ValueError:
        print('Error:enter numbers only')
    except ZeroDivisionError:
        print('error: enter non zero second inpt')
    except Exception as err:
        print('incorrect input')
        print(err)
        print(type(err))
    finally:
        print('thank youuu')


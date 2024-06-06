# gets the date, month, year and time.
import datetime
now = datetime.datetime.now()
date = now.strftime("%d-%m-%y %H:%M:%S")

# get the input from user/cashier.
cashier = input("Enter the cashier's name: ")
item_bought = input("Enter the product being bold: ")
item_cost = input("Enter the cost of the product: ")
total_items = input("Enter the number of products bought: ")
payment_method = input("Enter the payment method being used: ")
amount_presented = input("Enter the amount received from customer: ")

# processes the calculations.
total_cost = int(item_cost) * int(total_items)
change = int(amount_presented) - int(total_cost)

# prints the customer's receipt.
print("             BOXER            ")
print(" Never pay more than the Boxer price ")
print("     Customer Care-line 0860 02 69 37     ")
print("         POLOKWANE 2         ")
print("YOUR CASHIER IS      " + cashier)
print(""
      "")
print(f'{item_bought}   R{item_cost}          {item_cost}#')
print(f'TOTAL ITEMS     {total_items}       TOTAL       {total_cost}')
print(f'        {payment_method.upper()}                {amount_presented}')
print(f'        CHANGE                                {change}')
print(""
      "")
print(f'VAT INCLUDED    @       {15.0}%')
print(f'NON SUPPLY   e          ZERO RATED  #')
seperator = "-" * 14
print(f'{seperator}VAT REG NO.   4520103302{seperator}')
print(""
      "" * 2)
print("     THANK YOU FOR SHOPPING WITH US.     ")
print("           TAX INVOICE       ")
print("        PO Box 370 Westville 3630        ")
print("*6129 9333/005/114     " + f'{date} AC-00')
cut_here = "=" * 42
print(f'cut here{cut_here}')
print("     Topup             Voucher           ")
print("       HOLLY TOP UP VOUCHER")
print(""
      "" * 2)
print("     Voucher           Value     ")
print(f'      Total     R{total_cost}')
print(""
      "")
print("Ref: PP1118153556      Txn: PP1118153556")
print(""
      "")
print("     To redeem dial *120*HOLLY*5*Pin#")
print("     or visit www.hollywoodbets.mobi")
print("       Helpline Number 087 353 7634")
print(""
      "")
print("PIN:       2593354054054710658")
print(""
      "")
cut_here = "=" * 54
print(cut_here)
print(f'*6129 9333/005/114    {date} AC-00')
# Kayla Mabalot (@026840318)
# IS 340: 2023-10-09-07:00:PM
# Professor Phillips Austin

# The Haunted Boat Agency:

#PART 1- IN-PUT CRITERIA: Quantities & Qualities 

def main():
	    #WEB-MUSIC = YouTube background song for boat ride: Fantasy Ambiance - Lovecraft Ocean [YouTube]
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=LIk_HY-kuSc&t=42s")
    
		#LOOP: while loop in action 
    while True:
            print("________________________________\n\n\n\nHalloween Horror Nights\npresents... \nThe Haunted Boat Agency:")
            buy = input("\nTo Make Purchase(s): \n[Y] Yes, I'm Ready\n(N) No...I Quit\nEnter y or n: ")
            if buy == "y":
                print("\nWe hope you enjoy your time at the Haunted Boat Agency!\n")
                #USER-INPUT: Sections & Selections (A-D and Boat Size)  
                G = int(input("(A) How many GUEST(s) will be joining us today?\nEnter #: "))
                #print(guest, "x guests will be joining us today.")
                days = int(input("(B) How many DAY(s) will you be sailing with us?\nEnter #: "))
                #print(days,'x total days of sailing.')
                yacht = int(input("(C) How many guests are a MEMBER(s) of the Elite: Yacht Club?\nEnter #: "))
                #print(yacht,'x member(s) of yacht club') 
                scuba = int(input("(D) How many SCUBA GEAR(s) would you like to rent out?\nEnter #: "))
                #print(scuba,'x scuba gear(s).') 
                boat = int(input("\nSELECT: Boat 1 or 2 \n (1) The Black Jaws -------- $150 boat:40ft \n (2) The Baby Pirhana ----- $100 boat:30ft\nEnter 1 or 2: "))
#PART 2- OUT-PUT CRITERIA: Statements & Calculations
                print("\n________________________________\n\n(1) TICKET(s): The Haunted Boat Agency")
                print(G, "x Guest(s) will be joining us today")
                print(days,'x Day(s) of sailing')
                print(yacht,'x Member(s) of Yacht Club')
                print(scuba,'x Gear(s)')
                print("________________________________")
                #PER-PERSON|DAYS
                gear_price = ((scuba * 45.00) * days)
                yacht_discount = ((yacht * 0.15) * days)
                subtotal = (gear_price - yacht_discount)
                tax = subtotal * 0.095
                if boat == 1:
                    print("\n(2) BEWARE: The Black Jaws")
                    perp = ((G * 150.00) * days)
                    p1 = "{:.2f}".format(perp)
                    print(G, "x Ticket(s) for: $",p1)
                    x1 = int(perp + subtotal + tax)
                elif boat == 2:
                    print("\n(2) BEWARE: The Baby Pirhana")
                    perp2 = ((G * 100.00) * days)
                    p2 = "{:.2f}".format(perp2)
                    print(G, "x Ticket(s) for: $",p2)
                    x2 = int(perp2 + subtotal + tax)
                    #SUB•TOTALS: Scuba & Yacht
                yd = "{:.2f}".format(yacht_discount)
                gp = "{:.2f}".format(gear_price)
                print(" Scuba Gear: $", gp,"\n","Discount Yacht: -$",yd)
                sg = "{:.2f}".format(subtotal)
                print(" Subtotal: $", sg)
                if boat == 1:
                    y1 = "{:.2f}".format(x1)
                    print("TOTAL = $",y1)
                elif boat == 2:
                    y2 = "{:.2f}".format(x2)
                    print("TOTAL = $",y2)
                else:
                    print("N/A")
                # DATE AND TIME 
                from datetime import date 
                today = date.today()
                d4 = today.strftime("%d-%b-%Y")
                #Day-Month-Year
                print("Transaction Completed On:",d4)
                from datetime import datetime
                now = datetime.now()
                #YYYY-MM-DD HH:MM:SS
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                print(dt_string)


            elif buy == "n":
                print("\nThank you for your time! \n\nBeware... \nYou Must Come Back...\nOr else...")
                break
            else:
                print("Please enter 'y' or 'n'")
main()

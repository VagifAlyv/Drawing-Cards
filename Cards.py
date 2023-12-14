print("This program will draw two cards next to each other.")
print("─" * 20)

while True:
    print("Texts must not be empty.")
    card1_text = input("Text of first card: ")
    card2_text = input("Text of second card: ")
    print("─" * 20)

    card1_min_width = len(card1_text) + 2
    card2_min_width = len(card2_text) + 2

    print("Width of first card must be at least " + str(card1_min_width) + ".")
    card1_width = int(input("Width of first card: "))
    print("Width of second card must be at least " + str(card2_min_width) + ".")
    card2_width = int(input("Width of second card: "))
    print("─" * 20)

    print("Heights must be odd and at least 3.")
    card1_height = int(input("Height of first card: "))
    card2_height = int(input("Height of second card: "))
    print("─" * 20)

    is_invalid = (
        len(card1_text) == 0
        or len(card2_text) == 0
        or card1_width < card1_min_width
        or card2_width < card2_min_width
        or card1_height % 2 == 0
        or card2_height % 2 == 0
        or card1_height < 3
        or card2_height < 3
    )

    if is_invalid:
        print("ERROR: Invalid inputs. Please retry.")
    else:
        if card1_height == card2_height:

            w1 = card1_width - 2  
            w2 = card2_width - 2

            # height of the cards
            h = card1_height

            # Number of lines in upper_lines
            v = h - 3
            # Number of lines in lower_lines
            u = v // 2
            l = v - u

            # Total number of spaces in center_line 
            hz1 = w1 - len(card1_text) 
            hz2 = w2 - len(card2_text)

            # Number of spaces on the left of text, in center_line
            l1 = hz1 // 2 
            l2 = hz2 // 2

            # Number of spaces on the right of text, in center_line
            r1 = hz1- l1
            r2 = hz2 - l2

            # Border elements
            hz_line = '─'
            v_line = '│'
            top =  '┬'
            bottom = '┴'

            # Top line
            top_line = '┌'  + hz_line * w1 + top + hz_line * w2 + '┐' + "\n"

            # Upper line
            upper_lines = (v_line + " " * w1 + v_line + " " * w2 + v_line + "\n") * u

            # Center line
            center_line = v_line + " " * l1 + card1_text + " " * r1 + v_line + " " * l2 + card2_text + " " * r2 + v_line + "\n"
            
            # Lower line
            lower_lines = (v_line + " " * w1 + v_line + " " * w2 + v_line + "\n") * l
            
            # Bottom line
            bottom_line = '└' + hz_line * w1 + bottom + hz_line * w2 + '┘' + "\n"
            print(top_line + upper_lines + center_line + lower_lines + bottom_line)


            pass



    


        elif card1_height > card2_height:

            w1 = card1_width - 2 
            w2 = card2_width - 2 

            # Number of lines in lower_lines
            v1 = card1_height - 3
            v2 = card2_height - 3 

            # upper lines   
            u1 = v1 // 2 
            u2 = v2 //2

            # lower lines
            l1 = v1 - u1
            l2 = v2 - u2

            # Total number of spaces in center_line 
            hz1 = w1 - len(card1_text) 
            hz2 = w2 - len(card2_text)

            # Number of spaces on the left of text, in center_line
            left1 = hz1 // 2 
            left2 = hz2 // 2

            # Number of spaces on the right of text, in center_line
            r1 = hz1- left1 
            r2 = hz2 - left2
                
            # Border elements
            hz_line = '─' 
            v_line = '│' 

            # Top Line
            top_line = '┌' + hz_line * w1 + '┐' + '\n'

            # Upper Lines
            upper_lines1 = (v_line + " " * w1 + v_line + "\n") * (u2 - u1 - 1) 
            upper_lines2 = (v_line + " " * w1 + '├' + hz_line * w2 + '┐' + '\n' )
            upper_lines3 = (v_line + " " * w1 + v_line + " " * w2 + v_line + "\n" ) * (u2)
            upper_lines = upper_lines1 + upper_lines2 + upper_lines3

            # Center Line
            center_line = v_line + " " * left1 + card1_text + " " * r1 + v_line + " " * left2 + card2_text + " " * r2 + v_line + "\n"
            # Lower Lines
            lower_lines1 =(v_line + " " * w1 + v_line + " " * w2 + v_line + "\n") * (l2)
            lower_lines2 = (v_line + " " * w1 + '├' + hz_line * w2 + '┘' + "\n")
            lower_lines3 = (v_line + " " * w1 + v_line + "\n") * (l2 - l1 - 1)
            lower_lines = lower_lines1 + lower_lines2 + lower_lines3

            # Bottom line
            bottom_line = '└' + hz_line * w1 + '┘' + '\n'
            print(top_line + upper_lines + center_line + lower_lines + bottom_line) 
        
            pass

        else:

   
            w1 = card1_width - 2 
            w2 = card2_width - 2 

            # Number of lines in lower_lines
            v1 = card1_height - 3
            v2 = card2_height - 3 
            
            # Upper lines
            u1 = v1 // 2 
            u2 = v2 //2

            # Lower lines
            l1 = v1 - u1
            l2 = v2 - u2

            # Total number of spaces in center_line 
            h1 = w1 - len(card1_text) 
            h2 = w2 - len(card2_text)

            # Number of spaces on the left of text, in center_line
            left1 = h1 // 2   
            left2 = h2 // 2
        
            # Number of spaces on the right of text, in center_line
            r1 = h1- left1 
            r2 = h2 - left2

            # Border elements
            hz_line = '─' 
            v_line = '│' 

            top_line = (w1 + 1) * " " + '┌' + hz_line * w2 + '┐' + '\n'
            
            # Upper lines
            upper_lines1 = (' ' * (w1 + 1)  + v_line + " " * w2 + v_line + "\n") * (u1 - u2 - 1)
            upper_lines2 = ('┌' + hz_line * w1 + '┤' + ' ' * w2 + v_line + "\n")
            upper_lines3 = (v_line + " " * w1 + v_line + " " * w2 + v_line + "\n") * (u2)
            upper_lines = upper_lines1 + upper_lines2 + upper_lines3
            
            # Center line
            center_line = v_line + " " * left1 + card1_text + " " * r1 + v_line + " " * left2 + card2_text + " " * r2 + v_line + "\n"
            
            # Lower lines
            lower_lines_1 = (v_line + " " * w1 + v_line + " " * w2 + v_line + "\n") * (l1)
            lower_lines_2 = ('└' + hz_line * w1 + '┤' + ' ' * w2 + v_line + "\n")
            lower_lines_3 = (' ' * (w1 + 1) + v_line + ' ' * w2 + v_line + "\n") * (l1 - l2 - 1)
            lower_lines = lower_lines_1 + lower_lines_2 + lower_lines_3

            # Bottom line
            bottom_line = (w1 + 1) * ' ' + '└' + hz_line * w2  + '┘' + "\n"
            print(top_line + upper_lines + center_line + lower_lines + bottom_line)

        pass


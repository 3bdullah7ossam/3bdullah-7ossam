#Project: The Secure Massenger (symmetric Encryption tool)
#Author:Abdullah Hossam Shaban Kamel 
#Date : jan,2026
#Description:
#     Inspired by historical 'massengers' and the need for data privacy,
#     this script implements a custom Affine Cipher.
#     it uses modular Arthmetic to transform next into secure Code.
# Technical Logic
#          - Uses Modular Multiplicative Inverse for decryption.
#          - Configurable (e.g. , Mod 50 for English titel's and Characters).
#          - Designed for lightweight, secure massage exchange. 
#==============================================================================================================
Dect={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,
       "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":27,
       "!":28,":":29,"%":30,"$":31,"<":32,">":33,";":34,".":35,"\\":36,"=":37,"+":38,"*":39,"#":40,"}":41,
       "?":42,"|":43,"(":44,")":45,"^":46,"_":47,"-":48,"/":49,"@":50}

inve_Dect={v:k for k,v in Dect.items()}

# print(inve_Dect) invers dectionry

encr_massage="" #store of encryption

massage=input("Hello, Enter your massage\n").lower()

print(" ")

for i in massage:
    if i in Dect:
        x=Dect[i]
        f_x=x*3%50  # encryption equation 
        if f_x in inve_Dect:
            encr_massage+=inve_Dect[f_x]

print(f"{encr_massage}\n" "\nencryption is finshed.")

print("="*100)

Qustion=input("Do you back the next to orgnal text \nplease answer with yes or no \n").lower()

Orgnal_text=""

if Qustion=="no":
    print("encryption is finshed.")
elif Qustion=="yes":
    for i in encr_massage:
        if i in Dect:
            Back=Dect[i]*17%50
            if Back in inve_Dect:
                Orgnal_text+=inve_Dect[Back]
    print(f"Orgnal text is {Orgnal_text}")

else:
     print("please enter yes or no only ")





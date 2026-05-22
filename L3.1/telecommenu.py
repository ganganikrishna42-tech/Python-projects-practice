language = input("press 1 for english, 2 for hindi, 3 for Gujarati: ")

match language:
    case "1":
        print("you have selected english")
        english = input("press 4 to get the following services:" \
        "1. balance enquiry, 2. recharge, 3. customer care: ")
    case "2":
        print("you have selected hindi")
        hindi = input("निम्नलिखित सेवाओं का लाभ उठाने के लिए 4 दबाएँ:" \
        "1. बैलेंस की जानकारी, 2. रिचार्ज, 3. ग्राहक सेवा। ")
    case "3":
        print("you have selected Gujarati")
        gujarati = input("નીચે આપેલ સેવાઓ મેળવવા માટે 4 દબાવો:" \
        "1. બેલેન્સ પૂછપરછ, 2. રિચાર્જ, 3. ગ્રાહક સેવા: ")
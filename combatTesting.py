from FinalProject import Character

print("Initializing combat test")

unit1 = Character('Rey', 1, 'Player')
unit2 = Character('Not Rey', 1, 'Player')

print(unit1)
print(unit2)

unit1.combat(unit2)

print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWXKXNWWWWWMNKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMNxoooddxdkXxcOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWX000O0kkKNX0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0kxddddddddxk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0doooodxkkOOOOkxd;,OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMN0OkkkkOO0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxclx0NWMMMMMMMMMMMK:cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWd;lddddddoooooodkKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOcl0WMMMMMMMMMMMMMMNo:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMK:lNMMMMMMMMWNX0kdlld0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;dNMMMMMMMMMMMMMMMWx;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMO;dMMMMMMMMMMMMMMMWKdcoKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;oNMMMMMMMMMMMMMMMWk;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMO;xMMMMMMMMMMMMMMMMMWKl:0MMMMMMMMMMWNNXK00OOkkxxxxxxxxxxxkkkOO0KKXXl:KMMMMMMMMMMMMMMMWx;dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMO;xMMMMMMMMMMMMMMMMMMMX:cXNX0Oxddooooooooddddddxxxxxxxxxxddddddoool;;ldx0NWMMMMMMMMMXo:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM0:oWMMMMMMMMMMMMMMMMWXO;'coooddkO0KXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMWNNK0kdoloOWMMMMMWOcc0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXccXMMMMMMMMMMMMMMXxlloxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx:oNMWXklckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWx;kWMMMMMMMMMMMWk:l0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;cdolokNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXl:0WMMMMMMMMMNd;xWMMMMMMMMMWNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl.l0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXd:o0WMMMMMMWx;xWMMMMMMMMMMN0xooxKWMMMMMMMMMMMMMMMMMWWKk0NMMMMMMMMMMMMMMMMO;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWKdlloxOKXNO;oNMMMMMMMMMMMMMWXOdoOWMMMMMMMMMMMMMMMXd::dXWMMMMMMMMMMMMMMMMNccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWKkdoool':KMMMMWX0kxxOKNMMMMMNNWMMMMMMMMMMMMMMXdlx0WMWN0kxxk0NMMMMMMMMMx;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,xWMMWOc.     .,dXMMMMMMMMMMMMMMMMMMMMNXWMMW0l'.    .,oKWMMMMMMX:lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNccXMMNd.          ;0MMMMMMMMMMMMMMMMMMMMMMMWk.          'OMMMMMMWd;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;dWMMO.            cNMMMMMMMMMMMMMMMMMMMMMM0,            ;XMMMMMM0:oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo;0MMMx.            :XMMMMMMMMMMMMMMMMMMMMMMO.            ,KMMMMMMWo:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXclNMMMK;..         .dWMMMMMMMMMMMMMMMMMMMMMMXc...         lNMMMMMMMO;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;dWMMMW0c;;;;,,,..'dNMMMMMMMMMMMMMMMMMMMMMMMMKl;;;;,,,'..oXMMMMMMMMNccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd;OMMMMMMNOoooooloxKWMMMMMMMMMMMMMMMMMMMMMMMMMMN0dooooood0WMMMMMMMMMMx;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNccXMMMMMMMMMWNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXNNWMMMMMMMMMMMMMK:lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKOkxxxxOKNWMMMMMMMMMMMMMWd;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,kMMMMMMMMMMMMMWKkddoddoox0WMMMNX0O0KNMMMMNko:.'lxxxdolokNMMMMMMMMMMMM0;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0,,KMMMMMMMMMMWKdlloxO00o,'l0WMW0xdoodxONMMMMMWNOlcdXMMWXklcxNMMMMMMMMMMNl;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNc cNMMMMMMMMW0lcd0NMMNOlcxXWMMMWNNXK00KXNMMMMMMMMW0lcOWMMMWO:lKMMMMMMMMMMk.:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWd..dWMMMMMMMXo:dXMMMWOcckNMMMMN0xdoooddxOKWMMMMMMMMMNd;kWMMMMXl:0MMMMMMMMMX; :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMO;.,OMMMMMMW0cc0WMMMXo:xNMMMMMWXOOKXNWMMMMMMMMMMMMMMMMNo:0MMMMMXccKMMMMMMMMWd..cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMXc;;:XMMMMMWO:oXMMMM0ccKWMMMMMMMN0xdooooodOXMMMMMMMMMMMM0;oWMMMMM0;oWMMMMMMMM0;;;lXMMMMMMMMMMMMMMMMMMMMMMMMMMWXXWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWd;d:lNMMMMMO:oNMMMMK:lXMMMMMMMXxcldOKKXKOxlcoKWMMMMMMMMMX:lNMMMMMWo;0MMMMMMMMNl:d:oNMMMMMMMMMMMMMMMMMMMMMMMW0o;;kWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMO;dk;dMMMMMKccXMMMMWd;OMMMMMMWO:c0WMMMMMMMMWKo:kWMMMMMMMMK:oWMMMMMMO;xMMMMMMMMMk;xx;xWMMMMMMMMMMMMMMMMMMMMMKo:d0o;kWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXccXx;OMMMMWd;OMMMMMWo:0MMMMMM0:lNXOONMMMMKxxKNd;kMMMMMMMWx;kMMMMMMM0:oWMMMMMMMMX:lXo;OMMMMMMMMMMMMMMMMMMMNk:lKWMNl:0MMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWd;OWl:KMMMMXccNMMMMMMk;kMMMMMMd;OXc  cXMMX:  :XK:lWMMMMMMK:lNMMMMMWXd;kMMMMMMMMMWo;0XccXMMMMMMMMMMMMMMMMMKl:kWMMMMK:lXMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMO;oWXccNMMMMK:lWMMMMMMXc:KMMMMMx;OK,  ,KMMX:  :XK:lWMMMMW0ccKMWX0kdoloOWMMMMMMMMMMO;dW0;oNMMMMMMMMMMMMMMWO:lKMMMMMMMk;kMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXc:KM0:oWMMMMNc:XMMMMMMM0:lXMMMMKccKk::kWMMMXkkXNo;OMMMMXd''ldoooodk0NMMMMMMMMMMMMMNccXWx;kMMMMMMMMMMMMMWk:dNMMMMMMMMX:lNMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWx;kWMO;xMMMMMMO:l0WMMMMMM0cc0WMMM0cckXWMMMMMMMW0lcONX0kl,,:oxk0XWMMMMMMMMMMMMMMMMMMWd;0MNl:KMMMMMMMMMMMMk;dWMMMMMMMMMNl:KMMMMMMM
MMMMMMMMMMMMMMMMMMMMMK:lNMMx;OMMMMMMMXdlloxkO000x,'lxxxxo;.,lxO00Oxo;.'coollldOXWMMMMMMMMMMMMMMMMMMMMMMMMMx;OMM0;oWMMMMMMMMMMNccXMMMMMMMMMMNl:XMMMMMMM
MMMMMMMMMMMMMMMMMMMMWo;0MMWd;0MMMMMMMMMNKOxddddddoodxxxxxddllcllllccloxk0XWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl:XMMWd;OMMMMMMMMMMNl:KMMMMMMMMMM0:oWMMMMMMM
MMMMMMMMMMMMMMMMMMMM0;dWMMWd;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk;xWMMMXccXMMMMMMMMMM0ccONMNO0WMMKccKMMMMMMMM
MMMMMMMMMMMMMMMMMMMNl:KMMMMk;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:lNMMMMMk;xWMMMMMMMMMMXxllo:.lKOdcoKMMMMMMMMM
MMMMMMMMMMMMMMMMMMMO;dWMMMMNd;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:lXMMMMMMNl:KMMMMMMMMMMMMW0; .cooxKWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNl:KMMMMMMWk:lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:oXMMMMMMMMO;dWMMMMMMMMMMMWx'.cXWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMO;xWMMMMMMMMKo:dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd:xNMMMMMMMMMNo:KMMMMMMMMMMWx;,,kMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNl:KMMMMMMMMMMW0lcxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOcc0WMMMMMMMMMMM0;dWMMMMMMMMNd;o:cXMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMM0;dWMMMMMMMMMMMMWOlcxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo:xNMMMMMMMMMMMMMNl:KMMMMMMMNd:xd;kMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWd;OMMMMMMMMMMMMMMMNOlcxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKd:oKWMMMMMMMMMMMMMMMO;dWMMMMMKl:OO:oNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMXccNMMMMMMMMMMMMMMMMMW0ocdKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKocoKWMMMMMMMMMMMMMMMMMNccXMMMNk:lKXccKMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0;dWMMMMMMMMMMMMMMMMMMMW0ocoOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0ocoKWMMMMMMMMMMMMMMMMMMMMx;kWXkcckWXl:0MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMWXxclkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0lcdKWMMMMMMMMMMMMMMMMMMMMMMK;,lloONMXl:0MMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMNOlcd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNklcxXWMMMMMMMMMMMMMMMMMMMMMMMMNc'xXWMW0cc0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdclkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdclkNMMMMMMMMMMMMMMMMMMMMMMMMMMMWd;0MMXd:dXMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNklcoONMMMMMMMMMMMMMMMMMMMMMMMMWKxlco0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk;dOoco0WMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXxllox0XWMMMMMMMMMMMWWNXK0xdlloONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,,lxKWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMO;xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdoooodddddddddooooooodkKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;oWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOkkkkkkO0KXNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMX:lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO;dMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNl:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk;xMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx;OMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMO;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXccNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWd;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMM0;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNl:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMk;xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMXccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMk;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl:XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMk;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkloxXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNl:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXWMMMMMMMMMMMWXOoco0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMM0:lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkcdNMMMMMMMMMMMMMMWXd:oKWMMMMMMMMMMMMMMMMMMMMMMMMMMx;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWx;kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo:kNMMMMMMMMMMMMMMMMMMKo:kWMMMMMMMMMMMMMMMMMMMMMMMMNccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNl:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKcc0MMMMMMMMMMMMMMMMMMMMMWx;dNMMMMMMMMMMMMMMMMMMMMMMMO;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMKccXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKccKMMMMMMMMMMMMMMMMMMMMMMMWk;dNMMMMMMMMMMMMMMMMMMMMMWl:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMM0:oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKccXMMMMMMMMMMMMMMMMMMMMMMMMMWx;kWMMMMMMMMMMMMMMMMMMMM0;oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWO;oNMMMMMMMMMMMMMMMMMMMMMMMMMMMXccKMMMMMMMMMMMMMMMMMMMMMMMMMMMNl:KMMMMMMMMMMMMMMMMMMMWo:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWk;dNMMMMMMMMMMMMMMMMMMMMMMMMMNl:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:oWMMMMMMMMMMMMMMMMMM0:oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWk:oNMMMMMMMMMMMMMMMMMMMMMMMWd;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl,OMMMMMMMMMMMMMMMMMNl:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:lXMMMMMMMMMMMMMMMMMMMMMWk;xWMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkl:'lNMMMMMMMMMMMMMMMWx;kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKcc0WMMMMMMMMMMMMMMMMMMM0;cXMMMMMMMMMMMMMMMMMMMMMMMMWN0xoloOXd;OMMMMMMMMMMMMMMWO;dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo:kWMMMMMMMMMMMMMMMMMK:,cooxk0XNWWMMMMMMMMWWWNX0kdol,'dNMMMK:lNMMMMMMMMMMMMWO:oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;dNMMMMMMMMMMMMMMMXl:0NKOxo;,looooddddoooooooodk0Xx;kMMMMK;.kMMMMMNkOWMMWk:oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:oXMMMMMMMMMMMMMNo:OMMMMWk;dXNXKK00000KXXXNWMMMMM0;dWMWOc:,cXMMMK:.lNMXo:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0cc0MMMW0ldXMMMWd;kWMMMWO;oNMMMMMMMMMMMMMMMMMMMMMNl:OOl:xNO;oNNk:.'kXxcl0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo:kWMO:;;lNMWk.,0MMMWk;dNMMMMMMMMMMMMMMMMMMMMMMMXdloxXWMWOllllkl,cllONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx:ld:lXO;dNk;c:c0WXo:xNMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMWXNWMXkOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxokXMWk::;dNXdcolo0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKk0WMMWNKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMWNNWWWWMWWWWWWWWWMWWWWWWWWWNNWWMWWWWWWWWMWNNWWWWWWWWWWWMWWWWWWWWWWWWNNWMMMWWWWWNWMMWWWMMWWWMWWWWWWWWWMWNNWWWWWWWWWWWWWWWWWWWWWWWNNWWNNNWWWWWWWWWWMM
MMMWXXXXXNWXXXXXXXXXWNXKKXKKNNXKXXWNKKKXKKNWNKKXXXXXXXKKKKNNXXXKKXXXXXXKKXNMWNXXXKKXWNXXXNNKKNWNXXXXXXXXNXKKXXXXXXXKKKKKXXKKXXXXXXXKKXXKKXXNNXXXXXXNWM
MMMMWWWWWMMWWWWWWWWWMWWWWWNNWMWWWWMWWWWWNNWMWWWWWWWWWWWWXXWWWWWWWWWWWWWWWWWMMMWWWWWWMWWWWWWWWWMWWWMWWMWWWWWWWWWWWWWWWNXNWWWWWWWWWWWWWWWWWWWWWWWWWWWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""")
The level02 contains a `.pcap` file. It can be opened  with wireshark software.

Install wireshark on your local machine connected in ssh to the VM : 
```
sudo add-apt-repository universe
sudo apt install wireshark
```

Move the `.pcap` file locally : 

`scp -P 4242 level02@192.168.0.18:/home/user/level02/level02.pcap .`

We open the file with wireshark. There are 95 packets.

The 43rd packet present this peculiar data :  

```
0000   00 24 1d 0f 00 ad 08 00 27 cc 8a 1e 08 00 45 00   .$......'.....E.
0010   00 41 d4 b3 40 00 40 06 16 77 3b e9 eb df 3b e9   .A..@.@..w;...;.
0020   eb da 2f 59 99 4f ba a8 fb 18 9d 18 15 7b 80 18   ../Y.O.......{..
0030   01 c5 27 9d 00 00 01 01 08 0a 02 c2 3c 62 01 1b   ..'.........<b..
0040   b9 87 00 0d 0a 50 61 73 73 77 6f 72 64 3a 20      .....Password: 
```

If we take the hexa corresponding to 'password' it gives us the following string : `ft_wandr...NDRel.L0L.`

With 5 non-printable characters, which are [DEL] [DEL] [DEL] [DEL] [ENTER]

Re-writing the string with following the non-printable chars, we got this : `ft_waNDReL0L`

This is the correct password for `su flag02` !

`getflag` gives us the following token : `kooda2puivaav1idi4f57q8iq`

This token, given in input to `su level03` will lead us to level03
# Sources :

Install wireshark : 
- https://codepre.com/en/instalar-y-usar-wireshark-en-ubuntu-linux.html

Hexa to ascii converter : 
- https://www.rapidtables.com/convert/number/hex-to-ascii.html

ASCII Table – Hex to ASCII Value Character Code Chart :
- https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/

How to use wireshark :
- https://resources.infosecinstitute.com/topic/pcap-analysis-basics-with-wireshark/
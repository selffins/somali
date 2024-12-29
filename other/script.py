#!/usr/bin/env python3

x = """
daar	daarta	daaro
gees	geesta	geeso
laf	lafta	lafo
lug	lugta	luɣo
naag	naagta	naaɣo
tib	tibta	tiβo
sab	sabta	saβo
bad	bada	baðo
Jid	Jida	Jiðo
feeɖ	feeɖa	feeʐo
ʕiir	ʕiirta	ʕiiro
ʔul	ʔuʃa	ʔulo
bil	biʃa	bilo
meel	meeʃa	meelo
kaliil	kaliiʃa	kaliilo
najl	najʃa	najlo
sun	sunta	sumo
laan	laanta	laamo
sin	sinta	simo
dan	danta	dano
daan	daanta	daano
saan	saanta	saano
nirig	nirigta	nirgo
gaβaɖ	gaβaɖa	gabɖo
hoɣol	hoɣoʃa	hoglo
baɣal	baɣaʃa	baglo
waHar	waHarta	waHaro
irbad	irbada	irbaðo
kefed	kefeda	kefeðo
Jilin	Jilinta	Jilino
bohol	bohoʃa	boholo
jirid	jirida	jirdo
ʔaajad	ʔaajada	ʔaajaðo
gaʕan	gaʕanta	gaʕmo
ʔinan	ʔinanta	ʔinano
"""

chars = []
for c in x:
    chars.append(c)
unique_chars = list(sorted(list(set(chars))))
out = ""
consonants = ""
vowels = "aeiou"
for k in unique_chars:
    if k in vowels:
        continue
    consonants += " | " + k
for k in unique_chars:
    out += k
print("unique characters:")
print(out)
print("consonants")
print(consonants)
# "HJabdefghijklmnorstuwðɖɣʃʐʔʕβ"

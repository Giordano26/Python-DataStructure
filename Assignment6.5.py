text = "X-DSPAM-Confidence:    0.8475"
c1 = text.find('0')
c2 = text.find('5')
cf = float(text[c1:c2+1])
print(cf)

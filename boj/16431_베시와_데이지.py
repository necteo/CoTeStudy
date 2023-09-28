br,bc = map(int, input().split())
dr,dc = map(int, input().split())
jr,jc = map(int, input().split())

jbr = br-jr if br>=jr else jr-br
jbc = bc-jc if bc>=jc else jc-bc
jdr = dr-jr if dr>=jr else jr-dr
jdc = dc-jc if dc>=jc else jc-dc

jb = max(jbr,jbc)
jd = jdr+jdc

if jb < jd:
    print("bessie")
elif jb > jd:
    print("daisy")
else:
    print("tie")
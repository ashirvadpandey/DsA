    def secFrequent(self, arr, n):
        d={}
        for i in arr:
            c=arr.count(i)
            d[i]=c
        ans = sorted(d.values())
        chk=ans[-2]
        for k,v in d.items():
            if v==chk:
                return k
                

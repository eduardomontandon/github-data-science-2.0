def apura_area(votos_por_seçao, canditatos_por_partido):
    areas = []
    retorno  = {}
    partidos = {'fdb': 0, 'ipdt': 0}
    for i in votos_por_seçao:
        for j in i.keys():
            if j == 'area':
                if i['area']  not in areas:
                    areas.append(i['area'])
            if j == 'candidatos':
                for k in j.keys():
                    for z in canditatos_por_partido.values():
                        for t in z:
                            if t == k:
                    if fdb



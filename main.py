from morfeusz2 import Morfeusz
from concraft_pl2 import Concraft, Server

try:
    morfeusz = Morfeusz(expand_tags=True)
    server = Server(model_path="model.gz", port=3000)
    concraft = Concraft(port=3000)

    dag = morfeusz.analyse(u'W Szczebrzeszynie chrząszcz brzmi w trzcinie.')
    res = concraft.disamb(dag)
    print(res)

    dag = morfeusz.analyse(u'W Szczebrzeszynie chrząszcz brzmi w trzcinie.')
    dag_str = concraft.dag_to_str(dag)
    dag_disamb_str = concraft.disamb_str(dag_str)
    print(dag_disamb_str)
finally:
    server.terminate()
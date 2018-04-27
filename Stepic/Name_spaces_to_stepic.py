main_dicts = {'namespaces':{
    'global':{'parrent':'main_dicts',
              'namespaces':{},
              'variables':set()}}}

def adder(parrentNamespace,namespaceName, var):
    if namespaceName in parrentNamespace['namespaces']:
        if command == 'add':
            parrentNamespace['namespaces'][namespaceName]['variables'].add(var)
        elif command == 'create':
            parrentNamespace['namespaces'][namespaceName]['namespaces'].setdefault(var,{'parrent':namespaceName,
                                                                                                     'namespaces':{},
                                                                                                     'variables':set()})
        elif command == 'get':
            if var in parrentNamespace['namespaces'][namespaceName]['variables']:
                print(namespaceName)
                return
            else:
                if parrentNamespace['namespaces'][namespaceName]['parrent'] != 'main_dicts':
                    adder(main_dicts,parrentNamespace['namespaces'][namespaceName]['parrent'], var)
                else:
                    print('None')
                    return
        return
    else:
        for key in parrentNamespace['namespaces']:
            adder(parrentNamespace['namespaces'][key],namespaceName, var)

for i in range(int(input())):
    command, namespace, name = str.split(input())
    if command == 'add' or command == 'get':
        adder(main_dicts,namespace, name)
    elif command == 'create':
        adder(main_dicts, name, namespace)
                             
        

import os
try:
    from bomber import bomber
except:
    os.system('pip install arubomber')
    from bomber import bomber
bomber.main()
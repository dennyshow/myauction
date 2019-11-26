{"changed":true,"filter":false,"title":"views.py","tooltip":"/users/views.py","value":"from django.shortcuts import render\nfrom django.contrib.auth.models import User\nfrom .models import Profile\n\n\n# Create your views here.\n\ndef view_profile(request, profile_id):\n    try:\n        profile = Profile.objects.get(pk=profile_id)\n        \n        if profile.is_active:\n            return profile\n        return None\n    except Profile.DoesNotExist:\n        return None\n        \n    return render(request, \"profile.html\")","undoManager":{"mark":-2,"position":10,"stack":[[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":[","],"id":2}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":[" "],"id":3},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["p"]},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["r"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["o"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["f"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["i"]},{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":["l"]},{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["="],"id":4},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["N"]},{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["o"]},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["n"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":38},"end":{"row":7,"column":50},"action":"remove","lines":["profile=None"],"id":9},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"remove","lines":[" "]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"remove","lines":[","]}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":[" "],"id":10},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["u"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["s"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["e"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"remove","lines":["r"],"id":11},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"remove","lines":["e"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"remove","lines":["s"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["u"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["U"],"id":12},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["s"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["e"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["r"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":[","]}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"remove","lines":[","],"id":13},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"remove","lines":["r"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"remove","lines":["e"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"remove","lines":["s"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["U"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"remove","lines":[" "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":42},"action":"remove","lines":["return render(request, \"profile.html\")"],"id":14},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"insert","lines":[","],"id":15}],[{"start":{"row":9,"column":51},"end":{"row":9,"column":52},"action":"remove","lines":[","],"id":19}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":19},"end":{"row":13,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1574774756603}
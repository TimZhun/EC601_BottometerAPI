# EC601_BottometerAPI
Basic bototmeter API for Project 2
Barebones of botometer

**Code checks by username**
result = bom.check_account('@TamirlanN')
print(result)

**Code checks by ID**
result = bom.check_account(49124003)
print(result)


**results:**
{
'cap': <br />
{'english': 0.796599114745521, 'universal': 0.799570188835745},<br />
'display_scores': <br />
                {'english': <br />
                          {'astroturf': 0.1, 'fake_follower': 3.2, 'financial': 0.4, 'other': 2.6, 'overall': 3.2, 'self_declared': 0.0, 'spammer': 2.3}, 
                 'universal': <br />
                          {'astroturf': 0.0, 'fake_follower': 2.5, 'financial': 0.0, 'other': 1.2, 'overall': 1.8, 'self_declared': 0.4, 'spammer': 1.1}}, 
                 'raw_scores': <br />
                          {'english': <br />
                                    {'astroturf': 0.02, 'fake_follower': 0.64, 'financial': 0.07, 'other': 0.51, 'overall': 0.64, 'self_declared': 0.0, 'spammer': 0.47}, <br />
                          'universal': <br />
                                    {'astroturf': 0.0, 'fake_follower': 0.5, 'financial': 0.01, 'other': 0.25, 'overall': 0.36, 'self_declared': 0.08, 'spammer': 0.22}}, <br />
                          'user': <br />
                                    {'majority_lang': 'ru', 'user_data': {'id_str': '72018384', 'screen_name': 'TamirlanN'}<br />
       }<br />
}

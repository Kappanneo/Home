build: pym.py index.conf
	python2.7 pym.py index.conf > config

stable: config_stable
	cat config_stable > config

config_stable:
	wget -O config_stable "https://gitlab.com/kappanneo/home/raw/master/.i3/config"

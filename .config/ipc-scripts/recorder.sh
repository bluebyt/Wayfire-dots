#!/bin/sh

if pgrep -x wf-recorder >/dev/null; then
	printf '{"text":" On-air","class":"enabled"}';
else
	printf '{"text":" Off-air"}';
fi

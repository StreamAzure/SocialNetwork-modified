../wrk2/wrk -D exp -t 1 -c 1 -d 20 -L -s ./wrk2/scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R 1

../wrk2/wrk -D exp -t 1 -c 1 -d 20 -L -s ./wrk2/scripts/social-network/mixed-workload.lua -R 1
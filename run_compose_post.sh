../wrk2/wrk -D exp -t 3 -c 3 -d 60 -L -s ./wrk2/scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R 1
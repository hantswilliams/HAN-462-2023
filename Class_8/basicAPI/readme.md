# Deployment

## Render 
- trying to use render for the first time, sounds interesting // https://render.com/docs/deploy-flask 
- instructions: 
    - in my example, can keep the local main__ part of the bottom of the pyfile, since that is helpful for local deployment
    - when navigating into render, just need to select that it is a python app that will run on WSGI with gunicorn 
    - things to select: 
        - Env: `python` 
        - Build command: `pip install -r requirements.txt`
        - Start command: `gunicorn app:app` 
    - and thats it, should be up and running shortly 
    - currently have it configured so it re-deploys with each git push

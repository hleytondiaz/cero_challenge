## Cero Challenge
### Description
This project was developed to solve the challenge proposed by Cero through the following link: https://ceroai.notion.site/Ejercicio-t-cnico-para-integraciones-ba60159c762544648479a448bd8c0258. The solution basically consists of leveraging the Dentalink API to retrieve appointments and update one given its ID. Both integrations involve developing a client using FastAPI.

### Installation

Below are explained two ways to initialize the project. For both cases, it is necessary to complete the environment variables file named `.env`.

#### Manually

First, clone this repository.

```
git clone git@github.com:hleytondiaz/cero_challenge.git
```

Then, navigate to the `cero_challenge` directory.

```
cd cero_challenge
```

Next, create an environment named `cero_challenge` and activate it.

```
pip install virtualenv
virtualenv cero_challenge
source cero_challenge/bin/activate
```

Then, install the dependencies.

```
pip install -r requirements.txt
```

Finally, initialize the service. The API will be available at http://127.0.0.1:8000

```
uvicorn app:app --reload
```

#### Using Docker

First, clone this repository.

```
git clone git@github.com:hleytondiaz/cero_challenge.git
```

Then, navigate to the `cero_challenge` directory.

```
cd cero_challenge
```

Next, create the Docker image.

```
docker build -t cero_challenge .
```

Now, initialize the container under the name `cero_challenge`. The API will be available at http://127.0.0.1:8000

```
docker run --name cero_challenge -d -p 8000:8000 cero_challenge
```

### Usage Examples

#### Retrieve medical appointments

Given certain parameters indicated in the following cURL command, it is possible to retrieve medical appointments.

```
curl --location 'http://127.0.0.1:8000/citas/?id_branch=1&start_date=2024-02-12&end_date=2024-02-17' \
--header 'x-api-key: JF8XIOUK06387JJOE'
```

#### Update a medical appointment via an ID

Given an ID as a parameter and the new status as the body in the request, it's possible to update a medical appointment.

```
curl --location --request PUT 'http://127.0.0.1:8000/citas/328' \
--header 'x-api-key: JF8XIOUK06387JJOE' \
--header 'Content-Type: application/json' \
--data '{
    "id_status": 25
}'
```

### Testing

The `tests` directory includes several tests to test the API. The tests are run using the pytest package with the following command from the project's root directory.

```
python3 -m pytest
```

Then, you will be able to observe the test results as follows:

![Test results](https://iili.io/JEdFdAu.png)

### Additional Resources

Below are two links provided to download a Postman collection and its corresponding environment. The collection contains some endpoints about the Dentalink API and the endpoints of the developed API.

- Postman Collection: https://drive.google.com/file/d/1at4eqoOYKkic4zWUWbJ36SI4OqdSde2Q/view?usp=sharing
- Environment: https://drive.google.com/file/d/1lYZpmQFBRUBhqLQkAG7EhrTutdFOTg7O/view?usp=sharing

Once both files are imported, you will be able to see the following:

![Postman](https://iili.io/JEdFGNs.md.png)

### Contact

For any inquiries, feel free to connect with me on LinkedIn: https://www.linkedin.com/in/hleyton/.
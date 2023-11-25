from .http_response import HTTP_RESPONSE

class RESPONSE_SAMPLE:
  @staticmethod
  def BAD_REQUEST(details: dict = None) -> HTTP_RESPONSE:
    return HTTP_RESPONSE().withBody(
      message  = "Bad Request",
      state    = "failure",
      error    = True,
      data     = details
  ).withHeaders(content_type = "application/json").withStatus(400)

  @staticmethod
  def NOT_FOUND() -> HTTP_RESPONSE:
    return HTTP_RESPONSE().withBody(
      message  = "NOT FOUND",
      state    = "failure",
      error    = True
    ).withHeaders(content_type = "application/json").withStatus(404)

  @staticmethod
  def SERVER_ERROR() -> HTTP_RESPONSE:
    return HTTP_RESPONSE().withBody(
      message  = "INTERNAL SERVER error   ",
      state    = "failure",
      error    = True
    ).withHeaders(content_type = "application/json").withStatus(500)

  @staticmethod
  def CREATED(details: dict = None) -> HTTP_RESPONSE:
    return HTTP_RESPONSE().withBody(
      message  = "CREATED SUCCESSFULLY",
      state    = "SUCCESS",
      error    = False,
      data     = details
    ).withHeaders(content_type = "application/json").withStatus(201)

  @staticmethod
  def NOT_AUTHORIZED() -> HTTP_RESPONSE:
    return HTTP_RESPONSE().withBody(
      message  = "UNAUTHORIZED",
      state    = "failure",
      error    = True
    ).withHeaders(content_type = "application/json").withStatus(401)

  @staticmethod
  def OK(data = None) -> HTTP_RESPONSE:
    return HTTP_RESPONSE().withBody(
      message  = "OK",
      state    = "success",
      error    = False,
      data     = data    
    ).withHeaders(content_type = "application/json").withStatus(200)

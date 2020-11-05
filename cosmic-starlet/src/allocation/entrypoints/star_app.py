from starlette.applications import Starlette
from starlette.responses import JSONResponse
from datetime import datetime
import uvicorn

from allocation.domain import model
from allocation.adapters import orm
from allocation.service_layer import services, unit_of_work


app = Starlette(debug=True)


@app.route("/")
async def homepage(request):
    return JSONResponse({" Hello ": " World "})


@app.route("/add_batch", methods=["POST"])
async def add_batch(request):
    eta = request.json["eta"]
    if eta is not None:
        eta = datetime.fromisofformat(eta).date()
    services.add_batch(
        request.json["ref"],
        request.json["sku"],
        request.json["qty"],
        eta,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return JSONResponse({"OK": "201"})


@app.route("/allocate", methods=["POST"])
async def allocate_endpoint(request):
    try:
        batchref = services.allocate(
            request.json["orderid"],
            request.json["sku"],
            request.json["qty"],
            unit_of_work.SqlAlchemyUnitOfWork(),
        )
    except (services.InvalidSku) as e:
        return JSONResponse({"Message": str(e)})

    return JSONResponse({"batchref": batchref})


# Run with uvicorn

if __name__ == "__main__":
    uvicorn.run("star_app:app", host="127.0.0.1", port=8000, log_level="info")

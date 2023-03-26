import React, { Fragment, useRef, useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { toast } from "react-toastify";
import { useParams } from "react-router-dom";
import { Form, Button, Container, Row, Col, FloatingLabel } from "react-bootstrap"
import { LineWave } from "react-loader-spinner";
import {
    handleInput,
    loaderSize,
    loaderColor,
    validateEmpty,
} from "../../Utils/InputHelpers";
import { fetchProduct } from "../../Slicer/Product";
import { reseter, createOrder } from "../../Slicer/Order";
import { useNavigate } from "react-router-dom";

export const OrderForm = () => {
    const navigate = useNavigate();
    const { product_id } = useParams();
    const products = useSelector(fetchProduct);
    const productArray = Array.from(products)?.filter((product) => product.id == product_id)[0];
    const [orderData, setOrderData] = useState(
        {
            total_cost: "",
            phone_number: "",
            delivery_status: "",
            delivery_address: "",
            customer_id: "",
            products_id: "",
        }
    )
    const { status, message } = useSelector((state) => state.orders);
    const userx = localStorage.getItem("user")
        ? localStorage.getItem("user")
        : null;
    const user = JSON.parse(userx);
    console.log(user.id)
    const OrderStatus = ['pending', 'delivered']
    const orderOption = !OrderStatus
        ? ""
        : Array.from(OrderStatus)
            .sort((a, b) => {
                if (a.name < b.name) return -1;
                if (a.name > b.name) return 1;
                return 0;
            })
            .map((ord, index) => {
                return (
                    <option key={index} value={ord}>
                        {ord}
                    </option>
                );
            });

    const reset = () => {
        setOrderData({
            total_cost: "",
            phone_number: "",
            delivery_status: "",
            delivery_address: "",
            customer_id: "",
            products_id: "",
        });
    };
    const [formErrors, setFormErrors] = useState({});
    const [isSubmit, setIsSubmit] = useState(false);
    const referal = useRef();
    const dispatch = useDispatch();

    useEffect(() => {
        referal.current();
    }, [formErrors, status, message, dispatch]);

    const handleSubmit = (e) => {
        e.preventDefault();
        orderData.products_id = productArray.id
        orderData.customer_id = user.id
        orderData.total_cost = productArray.price
        console.log(orderData)
        setFormErrors(validateEmpty(orderData));
        setIsSubmit(true);
    };

    const dispatchCreation = () => {
        if (
            Object.keys(formErrors).length === 0 &&
            isSubmit &&
            status === "idle"
        ) {
            dispatch(createOrder(orderData));
            dispatch(reseter());
            setIsSubmit(false);
        }
        if (status === "succeeded") {
            toast.success("order created successfully", { autoClose: 2000 });
            reset();
            dispatch(reseter());
            setIsSubmit(false);
            setTimeout(() => navigate("/"), 1000);
        }
        if (formErrors?.all?.length > 1) {
            toast.error(formErrors?.all, { autoClose: 2000 });
        }
        if (status === "failed") {
            toast.error(message, { autoClose: 2000 });
            dispatch(reseter());
            setIsSubmit(false);
        }
    };
    referal.current = dispatchCreation;


    return (

        <Fragment>

            <Container fluid className="mt-5 mb-5 pt-5">
                <Row className="justify-content-center align-items-center">

                    <Col md={6}>
                        <h2 className="text-center text-uppercase"> Place Your Order for <p className="text-primary">{productArray?.title}</p></h2>
                        <Form onSubmit={handleSubmit}>
                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Label> Phone Number </Form.Label>
                                <Form.Control name="phone_number" type="text" placeholder="enter phone number" value={orderData.phone_number} onChange={(e) => handleInput(e, setOrderData)} />
                            </Form.Group>
                            <Form.Group className="mb-3">
                                <Form.Label>Status</Form.Label>
                                <Form.Select
                                    aria-label="Default select example"
                                    name="delivery_status"
                                    onChange={(e) => handleInput(e, setOrderData)}>
                                    <option>Select Status</option>
                                    {orderOption}
                                </Form.Select>
                            </Form.Group>
                            <FloatingLabel controlId="floatingTextarea2" label="delivery address">
                                <Form.Control
                                    as="textarea"
                                    value={orderData.delivery_address}
                                    onChange={(e) => handleInput(e, setOrderData)}
                                    name="delivery_address"
                                    placeholder="delivery address"
                                    style={{ height: '100px' }}
                                />
                            </FloatingLabel>
                            <div>
                                {status === "loading" ? (
                                    <LineWave
                                        color={loaderColor}
                                        height={loaderSize}
                                        width={loaderSize}
                                    />
                                ) : (
                                    <Button variant="primary" style={{backgroundColor: 'blue'}} type="submit">
                                        Submit
                                    </Button>
                                )}

                            </div>

                        </Form>

                    </Col>
                </Row>
            </Container>
        </Fragment>

    )
}

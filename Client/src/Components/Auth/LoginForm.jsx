import React, { useRef, useEffect, useState } from "react";
import { Form, Button } from 'react-bootstrap';
import { useDispatch, useSelector } from "react-redux";
import { toast } from "react-toastify";
import { useNavigate, useLocation } from "react-router-dom";
import { LineWave } from "react-loader-spinner";
import {
    handleInput,
    loaderSize,
    loaderColor,
    validateEmpty,
} from "../../Utils/InputHelpers";
import { reseter, login } from "../../Slicer/Auth";

const LoginForm = () => {
    const { user, status, message } = useSelector((state) => state.auth);
    const [loginData, setLogin] = useState({
        username: "",
        password: "",
    });
    const [formErrors, setFormErrors] = useState({});
    const [isSubmit, setIsSubmit] = useState(false);
    const referal = useRef();
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const location = useLocation();
    const from = location.state?.from?.pathname || "/";
    const redirector = () => {
        navigate(from, { replace: true });
    };

    const reset = () => {
        setLogin({
            username: "",
            password: "",
        });
    };

    useEffect(() => {
        referal.current();
    }, [formErrors, status, message, navigate, dispatch]);

    const handleLogin = (e) => {
        e.preventDefault();
        setFormErrors(validateEmpty(loginData));
        setIsSubmit(true);
    };

    const dispatchLogin = () => {
        if (
            Object.keys(formErrors).length === 0 &&
            isSubmit &&
            status === "idle"
        ) {
            dispatch(login(loginData));
            setIsSubmit(true);
        }

        if (status === "succeeded" || user) {
            if (isSubmit) {
                toast.success("login sucess");
                if (user) {
                    localStorage.setItem("user", JSON.stringify(user.data));
                }
                reset();
                reseter();
                setIsSubmit(false);
                redirector();
            }
        }
        if (status === "failed") {
            if (isSubmit) {
                toast.error(message, { autoClose: 4000 });
                setIsSubmit(false);
            }
        }
    };
    referal.current = dispatchLogin;
    return (
        <>
            <Form onSubmit={handleLogin}>

                <h2 className="text-center mb-5 p-4 text-light" style={{backgroundColor: '#5dbcd2'}}>
                    <i>
                        USER LOGIN
                    </i>
                </h2>
                <Form.Floating className="mb-3">
                    <Form.Control
                        id="floatingInputCustom"
                        type="text"
                        name="username"
                        placeholder="name@example.com"
                        value={loginData.username}
                        onChange={(e) => handleInput(e, setLogin)}
                    />
                    <label htmlFor="floatingInputCustom">Email/Username</label>
                </Form.Floating>
                <Form.Floating>
                    <Form.Control
                        id="floatingPasswordCustom"
                        type="password"
                        placeholder="Password"
                        name="password"
                        value={loginData.password}
                        onChange={(e) => handleInput(e, setLogin)}
                    />
                    <label htmlFor="floatingPasswordCustom">Password</label>
                </Form.Floating>
                <div>
                    {status === "loading" ? (
                        <LineWave
                            color={loaderColor}
                            height={loaderSize}
                            width={loaderSize}
                        />
                    ) : (
                        <Button variant="primary" style={{backgroundColor: '#5dbcd2'}} type="submit" className="mb-5 mt-5">
                            Submit
                        </Button>
                    )}

                </div>
            </Form>
        </>
    );
}

export default LoginForm;
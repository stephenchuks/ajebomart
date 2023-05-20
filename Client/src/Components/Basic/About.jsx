import React, { Fragment } from "react";
import { Row, Container, Card, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import wrash from "../../assets/img/wrash.jpg";

import { FaGit, FaPhoneAlt, FaGooglePlusG, FaLinkedin } from "react-icons/fa";
const About = () => {
  return (
    <Fragment>
      <Container fluid className="mt-5 pt-5 mb-5">
        <h3 className="text-center"> About-Us</h3>

        <Row className="justify-content-center mb-4">
          <Row className="justify-content-center">
            <div className="col-md-6 align-items-center abt">
              Our objective is to provide you with an unparalleled shopping
              experience, tailored to your unique needs and preferences. Our
              website is designed to be user-friendly, informative, and easy to
              navigate, and our team of experienced professionals is dedicated
              to delivering excellent customer service. We are always available
              to answer any questions, address concerns, and provide assistance
              whenever needed. We take pride in offering top-quality products at
              reasonable prices, sourcing from reputable suppliers to ensure the
              highest quality. We continually update our inventory with new and
              exciting products, so make sure to check back regularly. We
              appreciate you choosing AjeboMart, and we are excited to serve you
              and offer an exceptional shopping experience. If you have any
              inquiries or feedback, please don't hesitate to contact us.
            </div>
            <p />
          </Row>

          <Col className="col-md-6 d-flex">
            <Col md={4} className="text-center heit mx-auto w-76">
              <Card>
                <Card.Img
                  variant="top"
                  src={wrash}
                  className="pro_img"
                  alt="wrash"
                />
                <Card.Body>
                  <Card.Title>Chuks Humphrey Stephen</Card.Title>
                  <Card.Text>
                    {" "}
                    <i>Update Role Later</i>
                  </Card.Text>
                  <Card.Text>
                    +35795705939 <br />
                    <i>
                      stephenchuks@my.uopeople.edu <br />
                    </i>
                    <span className="flex-cls">
                      <FaGooglePlusG />
                      <Link to={"https://github.com/stephenchuks/"}>
                        {" "}
                        <FaGit className="text-primary " />{" "}
                      </Link>{" "}
                      <br />
                      <Link
                        to={
                          "https://www.linkedin.com/in/chuks-humphrey-stephen-614907165/"
                        }
                      >
                        {" "}
                        <FaLinkedin className="text-primary " />{" "}
                      </Link>
                      <FaPhoneAlt />
                    </span>
                  </Card.Text>
                </Card.Body>
              </Card>
            </Col>
            <Col md={4} className="text-center heit">
             
            </Col>
          </Col>
        </Row>
      </Container>
    </Fragment>
  );
};

export default About;

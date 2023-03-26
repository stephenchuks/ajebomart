import React from 'react'
import { Row, Col } from 'react-bootstrap';
const Footer = () => {
    return (
        <div className='footer'>
            <Row>
                <Col md={12} className="text-center">
                    <p>© 2023 AjeboMart Store. All rights reserved.</p>
                </Col>
            </Row>
        </div>
    )
}

export default Footer
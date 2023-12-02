import React, {useEffect, useState} from "react";
import styles from "./Auth.module.scss";
import Login from "./Login";
import {Card, Col, Row} from "antd";
import Register from "./Register";

enum TypeAuth {
    auth, register
}

const AuthWrapper: React.FC<any> = (props) => {
    const [type, setType] = useState<TypeAuth>(TypeAuth.auth);

    useEffect(() => {
        // if (props.auth) {
        //   navigate(prevLocation, { replace: true });
        // }
    }, [props.auth]);

    return (
        <Row className={styles.container}>
            <Col span={6} offset={9}>
                <Card>
                    {type === TypeAuth.auth ? <Login setRegisterForm={() => setType(TypeAuth.register)}/> :
                        <Register setAuthForm={() => setType(TypeAuth.auth)}/>}
                </Card>
            </Col>
        </Row>
    );
};

export default AuthWrapper;

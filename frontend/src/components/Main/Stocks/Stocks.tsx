import React, {FC, useState} from 'react';
import {Flex, Radio, RadioChangeEvent, Space} from "antd";
import styles from "./Stocks.module.scss";
import Stock from "./Stock";

const Stocks: FC = () => {
    const array = [
        {
            icon: '',
            text: 'Пивнуха'
        }
    ];

    const options = [
        {label: 'Взлеты дня', value: 'Взлеты дня'},
        {label: 'Падения дня', value: 'Падения дня'},
        {label: 'Взлеты дня1', value: 'Взлеты дня1'},
    ];

    for (let i = 0; i < 22; i++) {
        array.push({...array[0]});
    }

    const [value1, setValue1] = useState('Apple');

    const onChange1 = ({target: {value}}: RadioChangeEvent) => {
        console.log('radio1 checked', value);
        setValue1(value);
    };
    return (
        <>
            <div className={styles.listWrapper}>
                <Space className={styles.list}>
                    {array.map((value, index) => {
                        return <>
                            <Stock id={index} {...value}/>
                        </>
                    })}
                </Space>
            </div>
            <Flex gap={5} wrap={'nowrap'}>
                {/*<Radio.Group*/}
                {/*    options={options}*/}
                {/*    onChange={onChange1}*/}
                {/*    value={value1}*/}
                {/*    optionType="button"*/}
                {/*/>*/}
                {/*<Card className={styles.card} bordered={true} size={"small"}>Зашол на посашок</Card>*/}
            </Flex>
        </>
    );
};

export default Stocks;

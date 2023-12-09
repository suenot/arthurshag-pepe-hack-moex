import React, {memo, useEffect, useState} from 'react';
import {Line} from '@ant-design/plots';
import {mainApi} from "../../api/Api";
import {Datum} from "@ant-design/charts";
import {useParams} from "react-router-dom";

const Chart = memo(() => {
    const id = useParams().id;
    const [data, setData] = useState<any>([]);

    useEffect(() => {
        if (!id)
            return;
        asyncFetch(id);
    }, [id]);

    const asyncFetch = (id: any) => {
        mainApi.getChartStock(id)
            .then((json) => setData(json))
            .catch((error) => {
                console.log('fetch data failed', error);
            });
    };
    const config: any = {
        data,
        padding: 'auto',
        xField: 'trade_date',
        yField: 'close',
        xAxis: {
            tickCount: 5,
        },
        slider: {
            start: 0.1,
            end: 0.5,
        },
    };

    return <Line {...config} />;
});

export default Chart;

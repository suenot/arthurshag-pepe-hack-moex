import React from 'react';
import {Avatar, Flex, Space, Table as TableAnt, Tag} from 'antd';
import type {ColumnsType} from 'antd/es/table';
import {useNavigate} from "react-router-dom";

interface DataType {
    id: string;
    companyName: string;
    count: number;
    buyPrice: number;
    salePrice: number;
}

const columns: ColumnsType<DataType> = [
    {
        title: <div>Компания</div>,
        dataIndex: 'company',
        key: 'company',
        className: 'styles.row',
        render: (text, record) => <div>
            {record.companyName}
        </div>,
    },
    {
        title: <div>Кол-во</div>,
        dataIndex: 'count',
        key: 'count',
        className: 'styles.row',
        render: (text, record) => <div>
            {record.count}
        </div>,
    },
    {
        title: <div>Цена покупки</div>,
        dataIndex: 'purchasePrice',
        key: 'purchasePrice',
        className: 'styles.row',
        render: (text, record) => <div>
            {record.buyPrice}
        </div>,
    },
    {
        title: <div>Текущая цена</div>,
        dataIndex: 'currentPrice',
        key: 'currentPrice',
        className: 'styles.row',
        render: (text, record) => <div>
            {record.salePrice}
        </div>,
    },
];

const data: DataType[] = [
    {
        id: '1',
        companyName: 'СБЕР',
        count: 32,
        buyPrice: 100,
        salePrice: 96,
    },
    {
        id: '2',
        companyName: 'ARFLT',
        count: 250,
        buyPrice: 572,
        salePrice: 455,
    },
    {
        id: '3',
        companyName: 'Yandex',
        count: 33,
        buyPrice: 2178,
        salePrice: 1964,
    },
    {
        id: '4',
        companyName: 'MOEX',
        count: 856,
        buyPrice: 500,
        salePrice: 500000,
    }
];

const StockTable: React.FC = () => {
    const navigate = useNavigate();

    function onClick(): void {
        // navigate(`/card`);
    }

    return <TableAnt pagination={false} onRow={(record, rowIndex) => {
        return {
            onClick: onClick, // click row

        };
    }}
                     columns={columns} dataSource={data}/>;
};
export default StockTable;

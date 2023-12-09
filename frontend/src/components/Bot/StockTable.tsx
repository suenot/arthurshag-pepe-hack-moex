import React from 'react';
import {Avatar, Flex, Space, Table as TableAnt, Tag} from 'antd';
import type {ColumnsType} from 'antd/es/table';
import {useNavigate} from "react-router-dom";

interface DataType {
    key: string;
    name: string;
    age: number;
    address: string;
    tags: string[];
}

const columns: ColumnsType<DataType> = [
    {
        title: <div>Компания</div>,
        dataIndex: 'company',
        key: 'company',
        className: 'styles.row',
        render: (text, record) => <div>
            Сбер
        </div>,
    },
    {
        title: <div>Кол-во</div>,
        dataIndex: 'count',
        key: 'count',
        className: 'styles.row',
        render: (text, record) => <div>
            100
        </div>,
    },
    {
        title: <div>Кол-во</div>,
        dataIndex: 'count',
        key: 'count',
        className: 'styles.row',
        render: (text, record) => <div>
            100
        </div>,
    },
    {
        title: <div>Цена покупки</div>,
        dataIndex: 'purchasePrice',
        key: 'purchasePrice',
        className: 'styles.row',
        render: (text, record) => <div>
            100
        </div>,
    },
    {
        title: <div>Текущая цена</div>,
        dataIndex: 'currentPrice',
        key: 'currentPrice',
        className: 'styles.row',
        render: (text, record) => <div>
            100
        </div>,
    },
];

const data: DataType[] = [
    {
        key: '1',
        name: 'John Brown',
        age: 32,
        address: 'New York No. 1 Lake Park',
        tags: ['nice', 'developer'],
    },
    {
        key: '2',
        name: 'Jim Green',
        age: 42,
        address: 'London No. 1 Lake Park',
        tags: ['loser'],
    },
    {
        key: '3',
        name: 'Joe Black',
        age: 32,
        address: 'Sydney No. 1 Lake Park',
        tags: ['cool', 'teacher'],
    },
    {
        key: '3',
        name: 'Joe Black',
        age: 32,
        address: 'Sydney No. 1 Lake Park',
        tags: ['cool', 'teacher'],
    },
];

const StockTable: React.FC = () => {
    const navigate = useNavigate();

    function onClick(): void {
        navigate(`/card`);
    }

    return <TableAnt pagination={false} onRow={(record, rowIndex) => {
        return {
            onClick: onClick, // click row

        };
    }}
                     columns={columns} dataSource={data}/>;
};
export default StockTable;

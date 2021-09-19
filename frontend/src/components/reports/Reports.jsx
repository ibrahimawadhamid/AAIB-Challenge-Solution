import React, {useEffect, useState} from "react";
import axios from "axios";
import { Button, Col, Row } from 'react-bootstrap';
import "./reports.css";

axios.defaults.baseURL = process.env.REACT_APP_BACKEND_BASE_URL;

const Reports = () => {
    const [reports, setReports] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios.get("reports");
            console.log(result.data);
            setReports(result.data)
        };
        fetchData();
    }, []);

    const updateReportState = async (reportId, reportState) => {
        await axios.put(`reports/${reportId}`, { ticketState: reportState });
        const result = await axios.get("reports");
        console.log(result.data);
        setReports(result.data)
    };

    return (
        reports.map(report => (
            <Row key={report.id} className="report">
                <Col>
                    <Row>
                        <Col sm={6}>Id: {report.id}</Col>
                        <Col sm={3}>Type: {report.type}</Col>
                        <Col sm={3}><Button variant="danger" onClick={() => updateReportState(report.id, "BLOCKED")}>Block</Button></Col>
                    </Row>
                    <Row style={{marginTop: "1px"}}>
                        <Col sm={6}>State: {report.state}</Col>
                        <Col sm={3}>Message: {report.message}</Col>
                        <Col sm={3}><Button variant="success"
                        disabled={report.state === "CLOSED"}
                        onClick={() => updateReportState(report.id, "CLOSED")}>
                            Resolve</Button></Col>
                    </Row>
                    <Row>
                        <Col>
                        <a href="/">Details</a>
                        </Col>
                    </Row>
                </Col>
            </Row>
        ))
    )
}

export default Reports;
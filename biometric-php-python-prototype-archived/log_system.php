<?php

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $employee_id = $_POST['employee_id'];
    $name = $_POST['name'];
    $department = $_POST['department'];
    $timestamp = $_POST['timestamp'];
    $status = $_POST['status'];

    if (!$employee_id || !$name || !$timestamp || !$status || !$department) {
        echo json_encode([
            'status' => 'error',
            'message' => 'Missing required fields',
        ]);
        die();
    }

    $entry = [
        'employee_id' => $employee_id,
        'name' => $name,
        'department' => $department,
        'timestamp' => $timestamp,
        'status' => $status,
    ];

    $log_file = 'logs.json';
    $logs = [];

    if (file_exists($log_file)) {
        $logs = json_decode(file_get_contents($log_file), true);
        if (!is_array($logs)) {
            $logs = [];
        }
        $logs[] = $entry;
        file_put_contents($log_file, json_encode($logs, JSON_PRETTY_PRINT));
            
        echo json_encode(['status' => 'success','message' => 'Log saved']);
    }
} else {
    echo json_encode([
        'status' => 'error',
        'message' => 'Invalid request method'
    ]);
}
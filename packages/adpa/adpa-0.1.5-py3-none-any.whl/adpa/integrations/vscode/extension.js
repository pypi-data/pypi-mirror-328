const vscode = require('vscode');
const { spawn } = require('child_process');
const path = require('path');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    // Register commands
    let validateCommand = vscode.commands.registerCommand('adpa.validate', () => {
        runValidation();
    });
    
    let quickFixCommand = vscode.commands.registerCommand('adpa.quickFix', () => {
        applyQuickFix();
    });
    
    context.subscriptions.push(validateCommand);
    context.subscriptions.push(quickFixCommand);
    
    // Create status bar item
    const statusBarItem = vscode.window.createStatusBarItem(
        vscode.StatusBarAlignment.Right,
        100
    );
    statusBarItem.command = 'adpa.validate';
    context.subscriptions.push(statusBarItem);
    
    // Register diagnostic collection
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('adpa');
    context.subscriptions.push(diagnosticCollection);
    
    // File watcher for validation
    const fileWatcher = vscode.workspace.createFileSystemWatcher('**/*.{py,robot}');
    fileWatcher.onDidChange(uri => validateFile(uri, diagnosticCollection));
    fileWatcher.onDidCreate(uri => validateFile(uri, diagnosticCollection));
    context.subscriptions.push(fileWatcher);
    
    // Update status bar
    updateStatusBar(statusBarItem);
}

function deactivate() {}

async function runValidation() {
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders) {
        vscode.window.showErrorMessage('No workspace folder found');
        return;
    }
    
    const workspaceRoot = workspaceFolders[0].uri.fsPath;
    const pythonPath = await getPythonPath();
    
    const process = spawn(pythonPath, ['scripts/validate.py', 'quality', workspaceRoot]);
    
    let output = '';
    process.stdout.on('data', data => {
        output += data;
    });
    
    process.stderr.on('data', data => {
        console.error(`Error: ${data}`);
    });
    
    process.on('close', code => {
        if (code === 0) {
            const issues = JSON.parse(output);
            updateDiagnostics(issues);
            vscode.window.showInformationMessage('Validation complete');
        } else {
            vscode.window.showErrorMessage('Validation failed');
        }
    });
}

async function validateFile(uri, diagnosticCollection) {
    const pythonPath = await getPythonPath();
    const process = spawn(pythonPath, ['scripts/validate.py', 'quality', uri.fsPath, '--format', 'json']);
    
    let output = '';
    process.stdout.on('data', data => {
        output += data;
    });
    
    process.on('close', code => {
        if (code === 0) {
            const issues = JSON.parse(output);
            const diagnostics = issues.map(issue => {
                const range = new vscode.Range(
                    issue.line_number - 1,
                    0,
                    issue.line_number - 1,
                    1000
                );
                
                return new vscode.Diagnostic(
                    range,
                    issue.description,
                    mapSeverity(issue.severity)
                );
            });
            
            diagnosticCollection.set(uri, diagnostics);
        }
    });
}

function updateDiagnostics(issues) {
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('adpa');
    const diagnosticsMap = new Map();
    
    issues.forEach(issue => {
        const uri = vscode.Uri.file(issue.file_path);
        const diagnostics = diagnosticsMap.get(uri) || [];
        
        const range = new vscode.Range(
            issue.line_number - 1,
            0,
            issue.line_number - 1,
            1000
        );
        
        diagnostics.push(new vscode.Diagnostic(
            range,
            issue.description,
            mapSeverity(issue.severity)
        ));
        
        diagnosticsMap.set(uri, diagnostics);
    });
    
    diagnosticCollection.clear();
    for (const [uri, diagnostics] of diagnosticsMap) {
        diagnosticCollection.set(uri, diagnostics);
    }
}

function mapSeverity(severity) {
    switch (severity) {
        case 'high':
            return vscode.DiagnosticSeverity.Error;
        case 'medium':
            return vscode.DiagnosticSeverity.Warning;
        case 'low':
            return vscode.DiagnosticSeverity.Information;
        default:
            return vscode.DiagnosticSeverity.Hint;
    }
}

async function getPythonPath() {
    const pythonConfig = vscode.workspace.getConfiguration('python');
    return pythonConfig.get('defaultInterpreterPath') || 'python';
}

function updateStatusBar(statusBarItem) {
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (!workspaceFolders) {
        statusBarItem.hide();
        return;
    }
    
    statusBarItem.text = '$(beaker) ADPA';
    statusBarItem.tooltip = 'Run ADPA Framework validation';
    statusBarItem.show();
}

module.exports = {
    activate,
    deactivate
};

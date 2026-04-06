import 'package:flutter/material.dart';

void main() {
  runApp(const BootstrapApp());
}

class BootstrapApp extends StatelessWidget {
  const BootstrapApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: '__PROJECT_NAME__',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('__PROJECT_NAME__'),
        ),
        body: const Padding(
          padding: EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                '__PROJECT_PURPOSE__',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.w700),
              ),
              SizedBox(height: 16),
              Text('Framework: __FRAMEWORK__'),
              Text('Deployment: __DEPLOYMENT_TYPE__'),
              Text('Security: __SECURITY_PROFILE__'),
            ],
          ),
        ),
      ),
    );
  }
}

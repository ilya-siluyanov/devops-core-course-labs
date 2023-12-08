{{- define "app.env" -}}
env:
  - name: labno
    valueFrom:
     secretKeyRef:
          name: lab11-secret
          key: labno
{{- end -}}
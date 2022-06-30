from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from exam.serializer import ExamSerializer, ExamCreateSerializer
from exam.services import convert_document_to_images
from exam.models import Exam

class ExamViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Exam.objects.all()
        serializer = ExamSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        exam = Exam.objects.get(pk=pk)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)
    
    def create(self, request):
        if request.FILES.get('pdf_file') is None:
            return Response({'error': 'No file'}, status=403)
        
        serializer = ExamCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=403)
        
        urls = convert_document_to_images(
            pdf_file=request.FILES['pdf_file'],
            min_line_length=serializer.data['min_line_length'],
            max_line_gap=serializer.data['max_line_gap'],
            margin=serializer.data['margin']
        )
        return Response({'status':'ok', "info": urls}, status=200)


exam_list = ExamViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
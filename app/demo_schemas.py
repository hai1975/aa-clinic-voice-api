"""Field schemas per voice demo — synced with frontend demo-schemas.ts"""

DEMO_SCHEMAS: dict[str, dict] = {
    "00": {
        "title": {"vi": "Phiếu tư vấn Botox", "en": "Botox Consultation Record"},
        "doc_type": "form",
        "fields": [
            {"id": "honorific", "label": {"vi": "Danh xưng", "en": "Honorific"}},
            {"id": "inquiry_topic", "label": {"vi": "Nhu cầu tư vấn", "en": "Inquiry"}},
            {"id": "botox_history", "label": {"vi": "Tiền sử tiêm Botox", "en": "Botox history"}},
            {"id": "injection_history", "label": {"vi": "Lịch sử tiêm", "en": "Injection history"}},
            {"id": "safety_assessment", "label": {"vi": "Đánh giá an toàn", "en": "Safety assessment"}},
            {"id": "treatment_zones", "label": {"vi": "Vùng điều trị", "en": "Treatment zones"}},
            {"id": "estimated_units", "label": {"vi": "Định lượng Unit", "en": "Estimated units"}},
            {"id": "patient_name", "label": {"vi": "Họ và tên", "en": "Full name"}},
            {"id": "phone", "label": {"vi": "Số điện thoại", "en": "Phone number"}},
            {"id": "appointment_date", "label": {"vi": "Ngày hẹn", "en": "Appointment date"}},
            {"id": "appointment_time", "label": {"vi": "Giờ hẹn", "en": "Appointment time"}},
            {"id": "action_result", "label": {"vi": "Kết quả xử lý", "en": "Outcome"}},
        ],
    },
    "01": {
        "title": {"vi": "Phiếu đăng ký khám", "en": "Registration Form"},
        "doc_type": "form",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Họ và tên", "en": "Full name"}},
            {"id": "birthday", "label": {"vi": "Ngày sinh", "en": "Date of birth"}},
            {"id": "phone", "label": {"vi": "Số điện thoại", "en": "Phone number"}},
            {"id": "visit_reason", "label": {"vi": "Lý do khám", "en": "Visit reason"}},
        ],
    },
    "02": {
        "title": {"vi": "Lịch hẹn khám", "en": "Appointment Schedule"},
        "doc_type": "agenda",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Bệnh nhân", "en": "Patient"}},
            {"id": "symptoms", "label": {"vi": "Triệu chứng", "en": "Symptoms"}},
            {"id": "specialty", "label": {"vi": "Chuyên khoa", "en": "Specialty"}},
            {"id": "appointment_date", "label": {"vi": "Ngày hẹn", "en": "Date"}},
            {"id": "appointment_time", "label": {"vi": "Giờ hẹn", "en": "Time"}},
        ],
    },
    "03": {
        "title": {"vi": "Quy trình khám", "en": "Care Pathway"},
        "doc_type": "checklist",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Bệnh nhân", "en": "Patient"}},
            {"id": "current_step", "label": {"vi": "Bước hiện tại", "en": "Current step"}},
            {"id": "next_step", "label": {"vi": "Bước tiếp theo", "en": "Next step"}},
            {"id": "notes", "label": {"vi": "Ghi chú", "en": "Notes"}},
        ],
    },
    "04": {
        "title": {"vi": "Nhắc lịch dùng thuốc", "en": "Medication Reminder"},
        "doc_type": "form",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Bệnh nhân", "en": "Patient"}},
            {"id": "medicine_name", "label": {"vi": "Tên thuốc", "en": "Medicine"}},
            {"id": "dosage", "label": {"vi": "Liều lượng", "en": "Dosage"}},
            {"id": "schedule_time", "label": {"vi": "Giờ uống", "en": "Schedule"}},
        ],
    },
    "05": {
        "title": {"vi": "Phiếu sàng lọc", "en": "Triage Form"},
        "doc_type": "form",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Bệnh nhân", "en": "Patient"}},
            {"id": "main_symptoms", "label": {"vi": "Triệu chứng chính", "en": "Main symptoms"}},
            {"id": "urgency_level", "label": {"vi": "Mức độ khẩn cấp", "en": "Urgency"}},
            {"id": "recommended_action", "label": {"vi": "Hướng xử lý", "en": "Action"}},
        ],
    },
    "06": {
        "title": {"vi": "Phiếu hậu chẩn", "en": "Follow-up Record"},
        "doc_type": "form",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Bệnh nhân", "en": "Patient"}},
            {"id": "recovery_status", "label": {"vi": "Tình trạng", "en": "Recovery"}},
            {"id": "side_effects", "label": {"vi": "Tác dụng phụ", "en": "Side effects"}},
            {"id": "followup_date", "label": {"vi": "Tái khám", "en": "Follow-up date"}},
        ],
    },
    "07": {
        "title": {"vi": "Bệnh án giọng nói", "en": "Clinical Notes"},
        "doc_type": "notes",
        "fields": [
            {"id": "patient_name", "label": {"vi": "Bệnh nhân", "en": "Patient"}},
            {"id": "symptoms", "label": {"vi": "Triệu chứng", "en": "Symptoms"}},
            {"id": "diagnosis", "label": {"vi": "Chẩn đoán", "en": "Diagnosis"}},
            {"id": "prescription", "label": {"vi": "Đơn thuốc", "en": "Prescription"}},
        ],
    },
    "08": {
        "title": {"vi": "Phiếu tư vấn hotline", "en": "Hotline Inquiry"},
        "doc_type": "form",
        "fields": [
            {"id": "caller_name", "label": {"vi": "Người gọi", "en": "Caller"}},
            {"id": "inquiry_topic", "label": {"vi": "Nội dung hỏi", "en": "Topic"}},
            {"id": "resolution", "label": {"vi": "Giải đáp", "en": "Resolution"}},
        ],
    },
}


def get_schema(demo_id: str) -> dict:
    schema = DEMO_SCHEMAS.get(demo_id)
    if not schema:
        raise KeyError(f"Unknown demo_id: {demo_id}")
    return schema


def get_field_ids(demo_id: str) -> list[str]:
    return [f["id"] for f in get_schema(demo_id)["fields"]]


def format_fields_prompt(demo_id: str, lang: str) -> str:
    schema = get_schema(demo_id)
    is_vi = lang.startswith("vi")
    lines = []
    for f in schema["fields"]:
        label = f["label"].get("vi" if is_vi else "en", f["label"]["en"])
        lines.append(f'- {f["id"]}: {label}')
    return "\n".join(lines)
